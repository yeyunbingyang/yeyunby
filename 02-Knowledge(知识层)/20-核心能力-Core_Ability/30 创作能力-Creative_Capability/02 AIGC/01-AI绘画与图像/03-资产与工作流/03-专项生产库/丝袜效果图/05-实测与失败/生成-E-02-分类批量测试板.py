from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "06-交付样张" / "分类批量正式测试-E-02图案纹样"
OUTPUT = ROOT / "06-交付样张" / "分类批量正式测试-E-02图案纹样-PL-01-v01.png"

ITEMS = [
    ("01", "黑玫瑰", "玫瑰叶片贴合织物", "01-黑玫瑰.png"),
    ("02", "白色枝叶花", "白色枝叶清晰连续", "02-白色枝叶花.png"),
    ("03", "蝴蝶错落", "大小蝴蝶自然分布", "03-蝴蝶错落.png"),
    ("04", "单一动物纹", "单一斑马纹连续覆盖", "04-单一动物纹.png"),
    ("05", "星点节奏", "星点间距形成节奏", "05-星点节奏.png"),
    ("06", "规则波点", "圆点尺寸间距稳定", "06-规则波点.png"),
    ("07", "重复心形", "小型心形方向统一", "07-重复心形.png"),
    ("08", "水墨晕散", "安全拦截｜本轮未生成", None),
    ("09", "放射几何", "金黑放射阶梯结构", "09-放射阶梯几何.png"),
    ("10", "街头涂鸦", "涂鸦贴合腿部曲面", "10-街头涂鸦.png"),
    ("11", "云锦云纹", "金色云纹层次清楚", "11-云锦云纹.png"),
    ("12", "青花花草", "钴蓝花草对比清楚", "12-青花花草.png"),
]


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(Path("C:/Windows/Fonts") / name), size)


canvas = Image.new("RGB", (2160, 3840), "#F1EFEA")
draw = ImageDraw.Draw(canvas)
title_font = font("msyhbd.ttc", 92)
subtitle_font = font("msyh.ttc", 38)
name_font = font("msyhbd.ttc", 34)
desc_font = font("msyh.ttc", 25)
num_font = font("arialbd.ttf", 30)
footer_font = font("msyh.ttc", 27)

draw.text((96, 70), "E-02 图案与纹样", fill="#171717", font=title_font)
draw.text((98, 190), "12 种代表效果 · 亚洲成年女性商业展示 · 独立生成后确定性成板", fill="#55514B", font=subtitle_font)
draw.rounded_rectangle((1780, 78, 2064, 175), 44, fill="#171717")
draw.text((1844, 103), "05 / 09", fill="white", font=font("arialbd.ttf", 32))

left, top, gap_x, gap_y = 96, 310, 24, 26
cell_w, cell_h = 474, 1045
image_h = 845

for index, (number, name, desc, filename) in enumerate(ITEMS):
    row, col = divmod(index, 4)
    x = left + col * (cell_w + gap_x)
    y = top + row * (cell_h + gap_y)
    draw.rounded_rectangle((x, y, x + cell_w, y + cell_h), 24, fill="white")
    if filename:
        source = Image.open(SOURCE / filename).convert("RGB")
        fitted = ImageOps.fit(source, (cell_w, image_h), method=Image.Resampling.LANCZOS, centering=(0.5, 0.55))
        mask = Image.new("L", (cell_w, image_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, cell_w, image_h + 24), 24, fill=255)
        canvas.paste(fitted, (x, y), mask)
    else:
        draw.rounded_rectangle((x, y, x + cell_w, y + image_h), 24, fill="#E7E2DA")
        draw.ellipse((x + 183, y + 318, x + 291, y + 426), outline="#B7483B", width=10)
        draw.line((x + 207, y + 342, x + 267, y + 402), fill="#B7483B", width=10)
        draw.line((x + 267, y + 342, x + 207, y + 402), fill="#B7483B", width=10)
        failed_font = font("msyhbd.ttc", 30)
        draw.text((x + 136, y + 460), "本轮生成失败", fill="#7A3F37", font=failed_font)
    draw.rounded_rectangle((x + 18, y + 18, x + 84, y + 72), 18, fill="#171717")
    draw.text((x + 33, y + 27), number, fill="white", font=num_font)
    draw.text((x + 24, y + 870), name, fill="#171717", font=name_font)
    draw.text((x + 24, y + 930), desc, fill="#6A655E", font=desc_font)
    draw.line((x + 24, y + 988, x + cell_w - 24, y + 988), fill="#E3DED7", width=2)
    draw.text((x + 24, y + 1004), f"E-02 · {number}", fill="#9A938A", font=font("arial.ttf", 20))

footer_y = 3570
draw.line((96, footer_y, 2064, footer_y), fill="#CCC5BC", width=2)
draw.text((96, footer_y + 46), "说明：每格独立抽取基础 B，并叠加唯一扩展 E；模特、服装、姿势与构图按商品联动。", fill="#514D47", font=footer_font)
draw.text((96, footer_y + 102), "测试结果：11 / 12 成功；08 水墨晕散因安全拦截保留失败占位，不使用动漫或欧美回退。", fill="#7A3F37", font=footer_font)

canvas.save(OUTPUT, quality=95)
print(OUTPUT)
