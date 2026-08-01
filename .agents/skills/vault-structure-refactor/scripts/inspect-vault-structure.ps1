param(
    [Parameter(Mandatory = $true)]
    [string]$Path,

    [string]$OutputPath
)

$resolvedPath = (Resolve-Path -LiteralPath $Path -ErrorAction Stop).Path
$files = @(Get-ChildItem -LiteralPath $resolvedPath -Recurse -File -Force)
$directories = @(Get-ChildItem -LiteralPath $resolvedPath -Recurse -Directory -Force)
$markdown = @($files | Where-Object Extension -eq '.md')
$attachments = @($files | Where-Object Extension -in @('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.mp4', '.mov', '.pdf'))
$emptyDirectories = @($directories | Where-Object { @(Get-ChildItem -LiteralPath $_.FullName -Force).Count -eq 0 })

$versionPattern = '(?i)(?:^|[-_])(v\d+|版本\d*|新版|旧版|最终版|完整版|备份|副本)(?:[-_.]|$)'
$versionDocuments = @($files | Where-Object { $_.Extension -in @('.md', '.txt', '.docx', '.pdf') -and $_.Name -match $versionPattern })
$versionedAssets = @($files | Where-Object { $_.Extension -in @('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.mp4', '.mov') -and $_.Name -match $versionPattern })

$duplicateGroups = @()
$hashableFiles = @($files | Where-Object Length -gt 0)
if ($hashableFiles.Count -gt 0) {
    $duplicateGroups = @(Get-FileHash -LiteralPath $hashableFiles.FullName -Algorithm SHA256 |
        Group-Object Hash |
        Where-Object Count -gt 1 |
        ForEach-Object {
            [ordered]@{
                hash = $_.Name
                count = $_.Count
                paths = @($_.Group.Path | ForEach-Object { $_.Substring($resolvedPath.Length).TrimStart('\') })
            }
        })
}

$topDirectories = @(Get-ChildItem -LiteralPath $resolvedPath -Directory -Force | ForEach-Object {
    $children = @(Get-ChildItem -LiteralPath $_.FullName -Recurse -File -Force)
    [ordered]@{
        name = $_.Name
        files = $children.Count
        markdown = @($children | Where-Object Extension -eq '.md').Count
        attachments = @($children | Where-Object Extension -in @('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.mp4', '.mov', '.pdf')).Count
        size_mb = [math]::Round((($children | Measure-Object Length -Sum).Sum / 1MB), 2)
    }
})

$result = [ordered]@{
    root = $resolvedPath
    generated_at = (Get-Date).ToString('s')
    totals = [ordered]@{
        files = $files.Count
        directories = $directories.Count
        markdown = $markdown.Count
        attachments = $attachments.Count
        size_mb = [math]::Round((($files | Measure-Object Length -Sum).Sum / 1MB), 2)
    }
    top_directories = $topDirectories
    empty_directories = @($emptyDirectories | ForEach-Object { $_.FullName.Substring($resolvedPath.Length).TrimStart('\') })
    suspected_version_documents = @($versionDocuments | ForEach-Object { $_.FullName.Substring($resolvedPath.Length).TrimStart('\') })
    versioned_assets = @($versionedAssets | ForEach-Object { $_.FullName.Substring($resolvedPath.Length).TrimStart('\') })
    duplicate_hash_groups = $duplicateGroups
}

$json = $result | ConvertTo-Json -Depth 8
if ($OutputPath) {
    $parent = Split-Path -Parent $OutputPath
    if ($parent -and -not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Path $parent | Out-Null
    }
    Set-Content -LiteralPath $OutputPath -Value $json -Encoding utf8
}
$json
