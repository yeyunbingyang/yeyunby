# 合并重复笔记 & 清理 — 在终端执行: .\_merge_cleanup.ps1
$base = $PSScriptRoot

$merges = @(
    # 1. 基础知识: 保留基础.md(28KB) > 基础知识.md(26KB)
    @{ Old = "01-语法核心\01-基础\基础.md"; New = "01-语法核心\基础知识.md"; Action = "keep-old" },

    # 2. 正则: 保留 re模块.md(15KB) > 正则表达式.md(7KB)
    @{ Old = "02 标准库\re-正则表达式\re模块.md"; New = "02 标准库\re-正则表达式\正则表达式.md"; Action = "keep-old" },

    # 3. 异常处理: 合并两者
    @{ Old = "01-语法核心\06 异常处理\异常处理.md"; New = "01-语法核心\06 异常处理\错误和异常.md"; Action = "merge" },

    # 4. 函数: new(27KB) 替换 old(19KB)
    @{ Old = "01-语法核心\07 函数与模块\02 函数.md"; New = "01-语法核心\07 函数与模块\函数.md"; Action = "keep-new" },

    # 5. 模块与包: new(14KB) 替换 old(5KB)
    @{ Old = "01-语法核心\07 函数与模块\01 模块和包.md"; New = "01-语法核心\07 函数与模块\模块与包.md"; Action = "keep-new" },

    # 6. 面向对象入门: new(18KB) 替换 old(15KB)
    @{ Old = "01-语法核心\08 面向对象\01 面向对象编程入门.md"; New = "01-语法核心\08 面向对象\类和对象.md"; Action = "keep-new" },

    # 7. 面向对象进阶: 保留 old(19KB) > new(11KB)
    @{ Old = "01-语法核心\08 面向对象\02 面向对象编程进阶.md"; New = "01-语法核心\08 面向对象\三大特性.md"; Action = "keep-old" }
)

foreach ($m in $merges) {
    $oldPath = Join-Path $base $m.Old
    $newPath = Join-Path $base $m.New
    $oldName = Split-Path $m.Old -Leaf
    $newName = Split-Path $m.New -Leaf

    if (-not (Test-Path $oldPath)) { Write-Host "SKIP: old not found: $oldName" -ForegroundColor Yellow; continue }
    if (-not (Test-Path $newPath)) { Write-Host "SKIP: new not found: $newName" -ForegroundColor Yellow; continue }

    switch ($m.Action) {
        "keep-old" {
            Remove-Item $newPath -Force
            Write-Host "DELETE $newName (keep $oldName)" -ForegroundColor Green
        }
        "keep-new" {
            $newContent = [System.IO.File]::ReadAllText($newPath, [System.Text.Encoding]::UTF8)
            [System.IO.File]::WriteAllText($oldPath, $newContent, [System.Text.Encoding]::UTF8)
            Remove-Item $newPath -Force
            Write-Host "REPLACE $oldName <- $newName" -ForegroundColor Green
        }
        "merge" {
            $oldContent = [System.IO.File]::ReadAllText($oldPath, [System.Text.Encoding]::UTF8)
            $newContent = [System.IO.File]::ReadAllText($newPath, [System.Text.Encoding]::UTF8)
            $newBody = $newContent -replace '(?s)^---.*?---\r?\n', ''
            $merged = $oldContent.TrimEnd() + "`n`n---`n`n## 以下来自教材补充`n`n" + $newBody.TrimEnd() + "`n"
            [System.IO.File]::WriteAllText($oldPath, $merged, [System.Text.Encoding]::UTF8)
            Remove-Item $newPath -Force
            Write-Host "MERGE $newName -> $oldName" -ForegroundColor Green
        }
    }
}

# Also remove the monolithic source file (keeping it generates confusion)
$monolithic = Join-Path $base "尚硅谷大模型技术之Python1.0.md"
if (Test-Path $monolithic) {
    Remove-Item $monolithic -Force
    Write-Host "DELETE monolithic source file" -ForegroundColor Green
}

Write-Host "`nDone! 7 pairs merged, monolithic source removed." -ForegroundColor Cyan