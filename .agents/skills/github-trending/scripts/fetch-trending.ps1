<#
.SYNOPSIS
  抓取 GitHub 热门项目榜单（日榜/周榜/月榜 + 上周历史周榜）
.DESCRIPTION
  从 GitHub Trending 官方页面抓取 daily/weekly/monthly 榜单；
  上周周榜通过 Wayback Machine 快照还原；另用 GitHub Search API 补充上周新建热门仓库。
  输出 Markdown 文本。
.EXAMPLE
  powershell -File fetch-trending.ps1 -Top 10
#>
param(
    [int]$Top = 10,
    [switch]$SkipLastWeek
)

$ErrorActionPreference = 'Stop'
$ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
$tmp = Join-Path $env:TEMP 'github-trending'
New-Item -ItemType Directory -Force -Path $tmp | Out-Null

function Invoke-Curl([string]$Url, [string]$OutFile, [int]$TimeoutSec = 45) {
    & curl.exe -s -L --compressed --max-time $TimeoutSec -A $ua $Url -o $OutFile
    if ($LASTEXITCODE -ne 0 -or -not (Test-Path $OutFile)) { throw "抓取失败: $Url" }
    return (Get-Item $OutFile).Length
}
function ConvertTo-StripHtml([string]$s) {
    if ([string]::IsNullOrEmpty($s)) { return '' }
    $s = [regex]::Replace($s, '<[^>]+>', '')
    $s = $s -replace '&amp;', '&' -replace '&#39;', "'" -replace '&quot;', '"' -replace '&gt;', '>' -replace '&lt;', '<' -replace '&nbsp;', ' '
    return $s.Trim()
}

function Parse-TrendingPage([string]$Html) {
    $rows = [regex]::Matches($Html, '<article class="Box-row">([\s\S]*?)</article>')
    $list = @()
    $i = 0
    foreach ($m in $rows) {
        $row = $m.Groups[1].Value
        $i++
        $nameM = [regex]::Match($row, '<h2[^>]*>[\s\S]*?href="/([^"]+)"[\s\S]*?</h2>')
        $descM = [regex]::Match($row, '<p[^>]*class="col-9[^"]*"[^>]*>([\s\S]*?)</p>')
        $langM = [regex]::Match($row, 'itemprop="programmingLanguage">([^<]+)<')
        $starsM = [regex]::Match($row, 'href="/[^"]+/stargazers"[^>]*>([\s\S]*?)</a>')
        $trendM = [regex]::Match($row, 'class="d-inline-block float-sm-right"[^>]*>([\s\S]*?)</span>')
        if (-not $nameM.Success) { continue }
        $list += [pscustomobject]@{
            Rank  = $i
            Repo  = ConvertTo-StripHtml $nameM.Groups[1].Value
            Desc  = ConvertTo-StripHtml $descM.Groups[1].Value
            Lang  = ConvertTo-StripHtml $langM.Groups[1].Value
            Stars = ConvertTo-StripHtml $starsM.Groups[1].Value
            Trend = ConvertTo-StripHtml $trendM.Groups[1].Value
        }
    }
    return $list
}

function Format-Board([string]$Title, $List, [int]$Count) {
    $sb = [System.Text.StringBuilder]::new()
    [void]$sb.AppendLine("### $Title")
    $n = 0
    foreach ($r in $List | Select-Object -First $Count) {
        $n++
        $desc = if ($r.Desc) { $r.Desc } else { '无描述' }
        if ($desc.Length -gt 110) { $desc = $desc.Substring(0, 110) + '…' }
        $lang = if ($r.Lang) { "$($r.Lang)｜" } else { '' }
        [void]$sb.AppendLine("$n. [$($r.Repo)](https://github.com/$($r.Repo)) — $desc｜$lang★$($r.Stars)（$($r.Trend)）")
    }
    return $sb.ToString()
}

# ---------- 1. 官方日/周/月榜 ----------
$boards = @{}
foreach ($since in @('daily', 'weekly', 'monthly')) {
    $file = Join-Path $tmp "trending_$since.html"
    Invoke-Curl "https://github.com/trending?since=$since" $file | Out-Null
    $boards[$since] = Parse-TrendingPage (Get-Content -Raw -Encoding utf8 $file)
    Start-Sleep -Milliseconds 500
}

# ---------- 2. 上周榜（Wayback Machine） ----------
$lastWeek = $null
if (-not $SkipLastWeek) {
    $lastWeekDate = (Get-Date).AddDays(-7).ToString('yyyyMMdd')
    $wbFile = Join-Path $tmp 'wayback.json'
    try {
        Invoke-Curl "https://archive.org/wayback/available?url=github.com/trending%3Fsince%3Dweekly&timestamp=$lastWeekDate" $wbFile 30 | Out-Null
        $wb = Get-Content -Raw -Encoding utf8 $wbFile | ConvertFrom-Json
        if ($wb.archived_snapshots.closest.available) {
            $snapUrl = $wb.archived_snapshots.closest.url
            $snapTs   = $wb.archived_snapshots.closest.timestamp
            $rawUrl   = $snapUrl -replace '^http://', 'https://'
            $rawUrl   = $rawUrl -replace 'https://web\.archive\.org/web/', 'https://web.archive.org/web/'
            # 追加 id_ 取原始 HTML
            $rawUrl   = $rawUrl -replace '(/web/\d+)/', '$1id_/'
            $lwFile = Join-Path $tmp 'trending_lastweek.html'
            Invoke-Curl $rawUrl $lwFile | Out-Null
            $lastWeek = [pscustomobject]@{
                Date = $snapTs
                List = Parse-TrendingPage (Get-Content -Raw -Encoding utf8 $lwFile)
            }
        }
    } catch {
        Write-Warning "Wayback 上周快照获取失败: $($_.Exception.Message)"
    }
}

# ---------- 3. 上周新建热门仓库（Search API） ----------
$newRepos = @()
if (-not $SkipLastWeek) {
    $from = (Get-Date).AddDays(-7).ToString('yyyy-MM-dd')
    $to   = (Get-Date).ToString('yyyy-MM-dd')
    $searchFile = Join-Path $tmp 'search_created.json'
    try {
        Invoke-Curl "https://api.github.com/search/repositories?q=created:$from..$to&sort=stars&order=desc&per_page=10" $searchFile 45 | Out-Null
        $search = Get-Content -Raw -Encoding utf8 $searchFile | ConvertFrom-Json
        $newRepos = @($search.items | Select-Object -First 10 | ForEach-Object {
            [pscustomobject]@{
                Repo  = $_.full_name
                Desc  = $_.description
                Stars = $_.stargazers_count
            }
        })
    } catch {
        Write-Warning "Search API 获取失败: $($_.Exception.Message)"
    }
}

# ---------- 4. 输出 ----------
$today = (Get-Date).ToString('yyyy-MM-dd')
$out = [System.Text.StringBuilder]::new()
[void]$out.AppendLine("# GitHub 热门项目榜单（$today）")
[void]$out.AppendLine()
[void]$out.AppendLine('数据来源：GitHub Trending 官方页面（实时抓取）；上周榜来自 Wayback Machine 快照；上周新发布来自 GitHub Search API。')
[void]$out.AppendLine()
[void]$out.AppendLine((Format-Board "今日榜 Top $Top（since=daily）" $boards.daily $Top))
[void]$out.AppendLine()
[void]$out.AppendLine((Format-Board "本周榜 Top $Top（since=weekly）" $boards.weekly $Top))
[void]$out.AppendLine()
[void]$out.AppendLine((Format-Board "本月榜 Top $Top（since=monthly）" $boards.monthly $Top))
if ($lastWeek) {
    $snapDate = $lastWeek.Date
    $snapDate = "$($snapDate.Substring(0,4))-$($snapDate.Substring(4,2))-$($snapDate.Substring(6,2))"
    [void]$out.AppendLine()
    [void]$out.AppendLine((Format-Board "上周榜 Top $Top（Wayback 快照 $snapDate）" $lastWeek.List $Top))
}
if ($newRepos.Count -gt 0) {
    [void]$out.AppendLine()
    [void]$out.AppendLine("### 上周新发布热门 Top $($newRepos.Count)（created $from..$to）")
    $n = 0
    foreach ($r in $newRepos) {
        $n++
        $desc = if ($r.Desc) { $r.Desc } else { '无描述' }
        if ($desc.Length -gt 110) { $desc = $desc.Substring(0, 110) + '…' }
        [void]$out.AppendLine("$n. [$($r.Repo)](https://github.com/$($r.Repo)) — $desc｜★$($r.Stars)")
    }
}
[void]$out.AppendLine()

# 写入并回显
$outFile = Join-Path $tmp "github-trending-$today.md"
[System.IO.File]::WriteAllText($outFile, $out.ToString(), [System.Text.UTF8Encoding]::new($false))
Write-Output $out.ToString()
Write-Output ''
Write-Output "（已保存: $outFile）"
