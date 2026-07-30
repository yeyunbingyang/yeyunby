param(
    [Parameter(Mandatory = $true)]
    [string]$InputImage,

    [Parameter(Mandatory = $true)]
    [string]$OutputImage
)

Add-Type -AssemblyName System.Drawing

$canvasWidth = 1800
$canvasHeight = 2400
$headerHeight = 330
$outerMargin = 68
$gap = 24
$columns = 3
$rows = 2
$cardWidth = [int](($canvasWidth - 2 * $outerMargin - ($columns - 1) * $gap) / $columns)
$cardHeight = 930
$imageHeight = 748

$titleFont = New-Object System.Drawing.Font('Microsoft YaHei', 56, [System.Drawing.FontStyle]::Bold)
$eyebrowFont = New-Object System.Drawing.Font('Microsoft YaHei', 17, [System.Drawing.FontStyle]::Bold)
$subtitleFont = New-Object System.Drawing.Font('Microsoft YaHei', 24, [System.Drawing.FontStyle]::Regular)
$numberFont = New-Object System.Drawing.Font('Microsoft YaHei', 19, [System.Drawing.FontStyle]::Bold)
$nameFont = New-Object System.Drawing.Font('Microsoft YaHei', 24, [System.Drawing.FontStyle]::Bold)
$descriptionFont = New-Object System.Drawing.Font('Microsoft YaHei', 17, [System.Drawing.FontStyle]::Regular)
$footerFont = New-Object System.Drawing.Font('Microsoft YaHei', 15, [System.Drawing.FontStyle]::Regular)

$background = [System.Drawing.Color]::FromArgb(242, 238, 232)
$cardBackground = [System.Drawing.Color]::FromArgb(251, 249, 245)
$primaryText = [System.Drawing.Color]::FromArgb(43, 39, 36)
$secondaryText = [System.Drawing.Color]::FromArgb(112, 101, 92)
$accent = [System.Drawing.Color]::FromArgb(133, 104, 78)
$shadow = [System.Drawing.Color]::FromArgb(24, 55, 45, 38)

$items = @(
    @{ Number = '001'; Name = '正面平行'; Description = '整体透度 · 细闪密度' },
    @{ Number = '002'; Name = '轻微交叉'; Description = '腿部线条 · 脚踝贴合' },
    @{ Number = '003'; Name = '三分之四侧姿'; Description = '侧面轮廓 · 光泽变化' },
    @{ Number = '004'; Name = '沙发端坐'; Description = '膝部透感 · 纵向延伸' },
    @{ Number = '005'; Name = '坐姿腿部延伸'; Description = '暖光细闪 · 层次表现' },
    @{ Number = '006'; Name = '自然迈步'; Description = '动态贴合 · 鞋履衔接' }
)

$source = [System.Drawing.Image]::FromFile($InputImage)
$canvas = New-Object System.Drawing.Bitmap($canvasWidth, $canvasHeight)
$graphics = [System.Drawing.Graphics]::FromImage($canvas)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit
$graphics.Clear($background)

$leftFormat = New-Object System.Drawing.StringFormat
$leftFormat.Alignment = [System.Drawing.StringAlignment]::Near
$leftFormat.LineAlignment = [System.Drawing.StringAlignment]::Near

$rightFormat = New-Object System.Drawing.StringFormat
$rightFormat.Alignment = [System.Drawing.StringAlignment]::Far
$rightFormat.LineAlignment = [System.Drawing.StringAlignment]::Near

$primaryBrush = New-Object System.Drawing.SolidBrush($primaryText)
$secondaryBrush = New-Object System.Drawing.SolidBrush($secondaryText)
$accentBrush = New-Object System.Drawing.SolidBrush($accent)
$cardBrush = New-Object System.Drawing.SolidBrush($cardBackground)
$shadowBrush = New-Object System.Drawing.SolidBrush($shadow)
$accentPen = New-Object System.Drawing.Pen($accent, 4)

# 编辑式左对齐标题区，弱化“模板感”，强化商品系列层级。
$graphics.DrawString('LEGWEAR STUDY  ·  C05', $eyebrowFont, $accentBrush, [System.Drawing.RectangleF]::new($outerMargin, 48, 650, 36), $leftFormat)
$graphics.DrawString('丝袜上腿效果图鉴', $titleFont, $primaryBrush, [System.Drawing.RectangleF]::new($outerMargin, 91, 1100, 90), $leftFormat)
$graphics.DrawString('黑色半透细闪', $subtitleFont, $secondaryBrush, [System.Drawing.RectangleF]::new($outerMargin, 194, 500, 48), $leftFormat)
$graphics.DrawString('姿势展示案例  /  006 LOOKS', $eyebrowFont, $secondaryBrush, [System.Drawing.RectangleF]::new($canvasWidth - $outerMargin - 600, 204, 600, 40), $rightFormat)
$graphics.DrawLine($accentPen, $outerMargin, 275, $canvasWidth - $outerMargin, 275)

# 输入图固定为三列两行；逐格提取，图片保持大面积展示，文字作为轻量索引。
$sourceCellWidth = [int]($source.Width / 3)
$sourceCellHeight = [int]($source.Height / 2)

for ($index = 0; $index -lt 6; $index++) {
    $row = [int][math]::Floor($index / 3)
    $column = $index % 3
    $x = $outerMargin + $column * ($cardWidth + $gap)
    $y = $headerHeight + $row * ($cardHeight + $gap)

    $shadowRect = [System.Drawing.Rectangle]::new($x + 7, $y + 9, $cardWidth, $cardHeight)
    $graphics.FillRectangle($shadowBrush, $shadowRect)
    $cardRect = [System.Drawing.Rectangle]::new($x, $y, $cardWidth, $cardHeight)
    $graphics.FillRectangle($cardBrush, $cardRect)

    $sourceX = $column * $sourceCellWidth
    $sourceY = $row * $sourceCellHeight
    $sourceWidth = if ($column -eq 2) { $source.Width - $sourceX } else { $sourceCellWidth }
    $sourceHeight = if ($row -eq 1) { $source.Height - $sourceY } else { $sourceCellHeight }
    $sourceRect = [System.Drawing.Rectangle]::new($sourceX, $sourceY, $sourceWidth, $sourceHeight)
    $imageRect = [System.Drawing.Rectangle]::new($x, $y, $cardWidth, $imageHeight)
    $graphics.DrawImage($source, $imageRect, $sourceRect, [System.Drawing.GraphicsUnit]::Pixel)

    $item = $items[$index]
    $textX = $x + 26
    $textWidth = $cardWidth - 52
    $graphics.DrawString($item.Number, $numberFont, $accentBrush, [System.Drawing.RectangleF]::new($textX, $y + 773, 90, 34), $leftFormat)
    $graphics.DrawString($item.Name, $nameFont, $primaryBrush, [System.Drawing.RectangleF]::new($textX, $y + 814, $textWidth, 44), $leftFormat)
    $graphics.DrawString($item.Description, $descriptionFont, $secondaryBrush, [System.Drawing.RectangleF]::new($textX, $y + 867, $textWidth, 34), $leftFormat)
}

$footerY = $headerHeight + $rows * $cardHeight + ($rows - 1) * $gap + 30
$graphics.DrawLine($accentPen, $outerMargin, $footerY, $canvasWidth - $outerMargin, $footerY)
$graphics.DrawString('CORE  黑色半透 + 克制银色细闪', $footerFont, $secondaryBrush, [System.Drawing.RectangleF]::new($outerMargin, $footerY + 22, 700, 34), $leftFormat)
$graphics.DrawString('FORMAT  3:4  ·  腹部以下构图  ·  确定性文字排版', $footerFont, $secondaryBrush, [System.Drawing.RectangleF]::new($canvasWidth - $outerMargin - 800, $footerY + 22, 800, 34), $rightFormat)

$outputDirectory = Split-Path -Parent $OutputImage
if (-not (Test-Path -LiteralPath $outputDirectory)) {
    New-Item -ItemType Directory -Force -Path $outputDirectory | Out-Null
}

$canvas.Save($OutputImage, [System.Drawing.Imaging.ImageFormat]::Png)

$source.Dispose()
$graphics.Dispose()
$canvas.Dispose()
$titleFont.Dispose()
$eyebrowFont.Dispose()
$subtitleFont.Dispose()
$numberFont.Dispose()
$nameFont.Dispose()
$descriptionFont.Dispose()
$footerFont.Dispose()
$primaryBrush.Dispose()
$secondaryBrush.Dispose()
$accentBrush.Dispose()
$cardBrush.Dispose()
$shadowBrush.Dispose()
$accentPen.Dispose()
$leftFormat.Dispose()
$rightFormat.Dispose()

Write-Output $OutputImage
