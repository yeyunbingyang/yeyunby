from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math, json, os, shutil, hashlib, textwrap

ROOT = Path(__file__).resolve().parents[2]
LIB = ROOT / '01-公共资产库'
STAND = LIB / '02-多人站位'
STAND_CARDS = STAND / '01-词图卡'
STAND_DATA = STAND / '90-数据'
PROP = LIB / '05-道具与交互'
PROP_SEL = PROP / '01-道具选择器'
PROP_DATA = PROP / '90-数据'
ARCH = LIB / '99-归档'
for p in [STAND_CARDS, STAND_DATA, PROP_SEL, PROP_DATA, ARCH]: p.mkdir(parents=True, exist_ok=True)

FONT_REG = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
FONT_BOLD = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'

def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)

COL = {
    'navy': '#23364A', 'blue': '#3A6EA5', 'blue2': '#6E9DC8', 'orange': '#D9822B',
    'support': '#7B8794', 'light': '#F5F7FA', 'grid': '#D9E0E7', 'text': '#1F2933',
    'muted': '#5B6770', 'white': '#FFFFFF', 'green': '#3B7A57', 'red': '#B94A48',
    'cream': '#F7F1E8', 'yellow': '#E3B341', 'purple': '#7B61A8'
}

def wrap(draw, text, fnt, max_width):
    lines=[]
    cur=''
    for ch in str(text):
        test=cur+ch
        if draw.textbbox((0,0), test, font=fnt)[2] <= max_width:
            cur=test
        else:
            if cur: lines.append(cur)
            cur=ch
    if cur: lines.append(cur)
    return lines

def draw_wrapped(draw, xy, text, fnt, fill, max_width, line_gap=6, max_lines=None):
    x,y=xy
    lines=wrap(draw,text,fnt,max_width)
    if max_lines and len(lines)>max_lines:
        lines=lines[:max_lines]
        if lines:
            lines[-1]=lines[-1][:-1]+'…'
    h=0
    for line in lines:
        draw.text((x,y+h),line,font=fnt,fill=fill)
        h += fnt.size + line_gap
    return h

# --- standing cards ---
stand_specs = [
    dict(code='P2-01', title='双人并列', count=2, pos=[(.40,.52),(.60,.52)], angles=[90,90], protagonist=0,
         main='画面左或右三分位', direction='共同朝向镜头', spacing='约 0.8–1.2 个肩宽', camera='平视中景 / 全身', mood='平等、搭档、亲和',
         prompt='two people standing side by side, balanced spacing, both facing camera', fail='肩膀粘连、完全镜像、头高不一致'),
    dict(code='P2-02', title='前后错位', count=2, pos=[(.44,.63),(.61,.38)], angles=[90,90], protagonist=0,
         main='前景三分位', direction='同向或微侧向', spacing='前后 1–1.5 个身位', camera='轻微俯拍 / 中长焦', mood='主次、伙伴、叙事纵深',
         prompt='foreground lead, second person behind and offset, clear depth separation', fail='后排脸被挡、人物像叠在一起、透视比例失衡'),
    dict(code='P2-03', title='相对交流', count=2, pos=[(.38,.51),(.62,.51)], angles=[0,180], protagonist=0,
         main='左右对开', direction='彼此相向', spacing='1–1.5 个手臂长度', camera='侧向双人中景', mood='对话、协商、亲密',
         prompt='two people facing each other, conversational distance, open body language', fail='视线不相交、距离过近、手臂穿插'),
    dict(code='P2-04', title='背对张力', count=2, pos=[(.45,.51),(.55,.51)], angles=[180,0], protagonist=0,
         main='中心偏置', direction='背向相反方向', spacing='背部留 0.3–0.6 肩宽', camera='平视中景 / 广角', mood='冲突、决裂、双主角',
         prompt='two characters back to back, facing opposite directions, dramatic separation', fail='身体融合、背部重叠、双方主次不清'),
    dict(code='P2-05', title='主次高低', count=2, pos=[(.56,.47),(.35,.62)], angles=[90,45], scales=[1.12,.82], protagonist=0,
         main='主角站立居中', direction='主角面向镜头，配角侧向', spacing='水平 1–1.5 身位', camera='略低机位 / 中景', mood='权威、照顾、层级',
         prompt='standing lead with seated supporting person, clear height hierarchy', fail='坐姿高度不明、配角抢脸、比例变成巨人'),
    dict(code='P3-01', title='稳定三角', count=3, pos=[(.50,.63),(.34,.37),(.66,.37)], angles=[90,90,90], protagonist=0,
         main='前景顶点', direction='整体朝向镜头', spacing='横向 1–1.5 肩宽', camera='正面中景 / 全身', mood='团队、稳定、海报感',
         prompt='three-person triangular formation, lead in front, two behind', fail='三人同一水平线、后排遮脸、三角过窄'),
    dict(code='P3-02', title='中心主角', count=3, pos=[(.50,.51),(.30,.58),(.70,.58)], angles=[90,75,105], protagonist=0,
         main='画面中心', direction='配角微向主角', spacing='两侧各 1–1.5 身位', camera='正面平视 / 中景', mood='领袖、明星、介绍页',
         prompt='central lead with two supporting characters flanking, focus on center', fail='左右配角抢主角、完全对称僵硬、脸部同尺寸'),
    dict(code='P3-03', title='左右护卫', count=3, pos=[(.50,.60),(.28,.42),(.72,.42)], angles=[90,70,110], protagonist=0,
         main='前中景中心', direction='护卫外开或半侧', spacing='护卫距主角 1.5 身位', camera='轻微低机位 / 广角', mood='保护、权力、战队',
         prompt='lead in front center, two guards behind left and right, protective formation', fail='护卫比主角更近镜头、肩线重叠、阵型过散'),
    dict(code='P3-04', title='纵深队列', count=3, pos=[(.38,.66),(.51,.50),(.64,.34)], angles=[75,90,105], protagonist=0,
         main='前景起点', direction='沿对角线同向', spacing='每人间隔 1 个身位', camera='斜侧中长焦', mood='行进、时装、秩序',
         prompt='three people arranged in a diagonal depth line, staggered spacing', fail='人物完全遮挡、远近比例反转、队列贴边'),
    dict(code='PG-01', title='群像弧形', count=6, pos=[(.20,.52),(.31,.40),(.44,.34),(.56,.34),(.69,.40),(.80,.52)], angles=[75,80,90,90,100,105], protagonist=2,
         main='弧线中央', direction='整体朝中心或镜头', spacing='相邻 0.8–1.2 肩宽', camera='正面广角 / 全身', mood='庆典、团队、合照',
         prompt='group arranged in a gentle arc, central lead, faces clearly visible', fail='弧线变直线、边缘人物被裁、头部互相遮挡'),
    dict(code='PG-02', title='对称阵列', count=7, pos=[(.50,.62),(.35,.52),(.65,.52),(.22,.40),(.78,.40),(.39,.30),(.61,.30)], angles=[90]*7, protagonist=0,
         main='中轴前景', direction='统一正向', spacing='沿中轴对称展开', camera='正面低机位 / 广角', mood='仪式、组织、史诗',
         prompt='symmetrical group formation, central lead on axis, ordered rows', fail='中轴偏移、两侧人数不平衡、完全复制脸'),
    dict(code='PG-03', title='前中后景层次', count=6, pos=[(.38,.69),(.62,.69),(.27,.48),(.50,.48),(.73,.48),(.50,.28)], angles=[90]*6, protagonist=0,
         main='前景双主位之一', direction='统一或轻微内收', spacing='三层深度清晰', camera='中长焦 / 轻俯拍', mood='剧情群像、复杂关系',
         prompt='group in foreground midground background layers, clear depth hierarchy', fail='后排过小、层级挤成一团、焦点平均'),
    dict(code='PG-04', title='疏密节奏', count=6, pos=[(.24,.40),(.33,.46),(.26,.58),(.39,.60),(.66,.42),(.79,.60)], angles=[90,80,95,90,100,90], protagonist=1,
         main='密集组核心', direction='密集组内聚，疏组外开', spacing='一侧紧密、一侧留白', camera='横向广角 / 环境人像', mood='街拍、社交、叙事留白',
         prompt='asymmetrical group spacing, clustered figures balanced by isolated figures and negative space', fail='随机散点、留白无意义、主角落在边缘'),
]

def draw_camera(draw, cx, cy):
    draw.rounded_rectangle((cx-38,cy-22,cx+38,cy+22),radius=8,outline=COL['navy'],width=3,fill=COL['white'])
    draw.ellipse((cx-12,cy-12,cx+12,cy+12),outline=COL['navy'],width=3)
    draw.polygon([(cx+38,cy-12),(cx+58,cy-22),(cx+58,cy+22),(cx+38,cy+12)],outline=COL['navy'],fill=COL['white'])
    draw.text((cx-29,cy+30),'镜头',font=font(22),fill=COL['muted'])

def draw_person(draw, x, y, angle, idx, main=False, scale=1.0):
    r=int(34*scale)
    fill=COL['orange'] if main else COL['blue2']
    outline=COL['navy']
    # shoulder ellipse + head circle
    draw.ellipse((x-r*1.2,y-r*.35,x+r*1.2,y+r*.55),fill=fill,outline=outline,width=3)
    draw.ellipse((x-r*.58,y-r*1.15,x+r*.58,y),fill=COL['white'],outline=outline,width=3)
    # facing arrow
    rad=math.radians(angle)
    start=(x,y-r*1.35)
    length=55*scale
    ex=start[0]+math.cos(rad)*length
    ey=start[1]+math.sin(rad)*length
    draw.line((start[0],start[1],ex,ey),fill=COL['red'] if main else COL['navy'],width=5)
    ah=12
    for da in (150,-150):
        rr=math.radians(angle+da)
        draw.line((ex,ey,ex+math.cos(rr)*ah,ey+math.sin(rr)*ah),fill=COL['red'] if main else COL['navy'],width=5)
    label='主' if main else str(idx+1)
    bb=draw.textbbox((0,0),label,font=font(24,True))
    draw.ellipse((x-r*1.05,y+r*.55,x-r*.05,y+r*1.55),fill=COL['orange'] if main else COL['support'])
    draw.text((x-r*.82,y+r*.66),label,font=font(24,True),fill=COL['white'])

def make_stand_card(spec):
    W,H=1800,1120
    im=Image.new('RGB',(W,H),COL['white']); d=ImageDraw.Draw(im)
    # Header
    d.rectangle((0,0,W,118),fill=COL['navy'])
    d.text((60,27),f"{spec['code']}  {spec['title']}",font=font(54,True),fill=COL['white'])
    d.text((W-450,40),'多人物站位词—图卡',font=font(30),fill='#DCE6F0')
    # diagram panel
    px0,py0,px1,py1=55,160,1150,1020
    d.rounded_rectangle((px0,py0,px1,py1),radius=22,fill=COL['light'],outline=COL['grid'],width=3)
    # rule-of-thirds and depth guides
    for frac in (1/3,2/3):
        x=px0+(px1-px0)*frac; y=py0+(py1-py0)*frac
        d.line((x,py0+28,x,py1-28),fill=COL['grid'],width=2)
        d.line((px0+28,y,px1-28,y),fill=COL['grid'],width=2)
    # perspective depth labels
    d.text((px0+25,py0+20),'后景',font=font(24),fill=COL['muted'])
    d.text((px0+25,(py0+py1)//2-10),'中景',font=font(24),fill=COL['muted'])
    d.text((px0+25,py1-52),'前景',font=font(24),fill=COL['muted'])
    # camera
    draw_camera(d,(px0+px1)//2,py1-58)
    # positions
    scales=spec.get('scales',[1]*len(spec['pos']))
    for i,((nx,ny),ang,sc) in enumerate(zip(spec['pos'],spec['angles'],scales)):
        x=px0+110+nx*(px1-px0-220)
        y=py0+65+ny*(py1-py0-180)
        draw_person(d,x,y,ang,i,main=(i==spec['protagonist']),scale=sc)
    # legend
    d.rounded_rectangle((px0+24,py1-118,px0+330,py1-68),radius=12,fill=COL['white'],outline=COL['grid'])
    d.ellipse((px0+42,py1-107,px0+76,py1-73),fill=COL['orange'],outline=COL['navy'])
    d.text((px0+90,py1-107),'主角 / 视觉焦点',font=font(24),fill=COL['text'])
    # Sidebar
    sx0,sy0,sx1,sy1=1190,160,1745,1020
    d.rounded_rectangle((sx0,sy0,sx1,sy1),radius=22,fill=COL['white'],outline=COL['grid'],width=3)
    rows=[('人数',f"{spec['count']} 人"),('主角位置',spec['main']),('朝向',spec['direction']),('间距',spec['spacing']),('镜头',spec['camera']),('适用情绪',spec['mood'])]
    y=190
    for k,v in rows:
        d.text((1225,y),k,font=font(25,True),fill=COL['blue'])
        h=draw_wrapped(d,(1380,y),v,font(25),COL['text'],330,line_gap=4,max_lines=2)
        y += max(62,h+18)
        d.line((1225,y-10,1710,y-10),fill=COL['grid'],width=1)
    # prompt and fail boxes
    d.rounded_rectangle((1220,y+5,1715,y+142),radius=14,fill='#EEF4FA')
    d.text((1240,y+20),'提示词片段',font=font(24,True),fill=COL['blue'])
    draw_wrapped(d,(1240,y+57),spec['prompt'],font(21),COL['text'],445,line_gap=3,max_lines=3)
    y2=y+162
    d.rounded_rectangle((1220,y2,1715,y2+145),radius=14,fill='#FBF0EF')
    d.text((1240,y2+15),'常见失败',font=font(24,True),fill=COL['red'])
    draw_wrapped(d,(1240,y2+53),spec['fail'],font(23),COL['text'],445,line_gap=4,max_lines=3)
    # footer
    d.text((60,H-62),'读图顺序：先定主角 → 再定朝向 → 再定间距与深度 → 最后选镜头。',font=font(27,True),fill=COL['navy'])
    path=STAND_CARDS/f"{spec['code']}-{spec['title']}.png"
    im.save(path,optimize=True)
    return path

stand_paths=[make_stand_card(s) for s in stand_specs]

# Contact sheet helper

def contact_sheet(paths, out, title, cols=4, thumb=(420,260), label=True, bg=COL['white']):
    margin=42; header=120; gap=25
    rows=math.ceil(len(paths)/cols)
    W=margin*2+cols*thumb[0]+(cols-1)*gap
    cell_h=thumb[1]+55 if label else thumb[1]
    H=header+margin+rows*cell_h+(rows-1)*gap+margin
    im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,header),fill=COL['navy'])
    d.text((margin,26),title,font=font(48,True),fill=COL['white'])
    for i,p in enumerate(paths):
        r,c=divmod(i,cols); x=margin+c*(thumb[0]+gap); y=header+margin+r*(cell_h+gap)
        src=Image.open(p).convert('RGB')
        src.thumbnail(thumb,Image.Resampling.LANCZOS)
        canvas=Image.new('RGB',thumb,COL['light'])
        canvas.paste(src,((thumb[0]-src.width)//2,(thumb[1]-src.height)//2))
        im.paste(canvas,(x,y))
        d.rectangle((x,y,x+thumb[0],y+thumb[1]),outline=COL['grid'],width=2)
        if label:
            name=Path(p).stem
            d.text((x,y+thumb[1]+10),name,font=font(24,True),fill=COL['text'])
    im.save(out,quality=92,optimize=True)

stand_index=STAND/'多人站位-视觉索引-v01.jpg'
contact_sheet(stand_paths,stand_index,'02-多人站位｜双人・三人・群像首批词—图卡',cols=4,thumb=(390,242))

# --- Prop selector sheets ---
props = {
'办公': [
 ('办公桌','office desk','建立工作界面','主体前方或侧前方'),('人体工学椅','ergonomic chair','专业、现代','桌后，避免遮腿'),
 ('笔记本电脑','open laptop','数字工作感','桌面主道具'),('显示器','desktop monitor','技术/设计岗位','背景侧后方'),
 ('记事本','notebook','记录与计划','手边或桌角'),('签字笔','pen','细节动作','与记事本配对'),
 ('咖啡杯','ceramic mug','松弛、日常','远离键盘核心区'),('台灯','desk lamp','局部光源','桌面边缘'),
 ('绿植','small potted plant','柔化硬朗空间','背景或桌角'),('文件架','file organizer','秩序、行政感','背景层'),
 ('玻璃隔断','glass partition','开放办公','后景结构'),('百叶窗','window blinds','商务光影','后景窗面')],
'居家': [
 ('沙发','fabric sofa','舒适、亲和','人物后方或坐姿载体'),('单椅','accent chair','独立、精致','侧后方'),
 ('圆形边桌','round side table','柔和构图','沙发或椅侧'),('地毯','textured rug','稳定地面层次','人物脚下'),
 ('落地灯','floor lamp','温暖生活感','画面边缘'),('靠垫','soft cushion','丰富质感','沙发上，数量 1–3'),
 ('盖毯','throw blanket','松弛、季节感','沙发扶手'),('书籍','stack of books','文化、生活痕迹','桌面或边柜'),
 ('花瓶','ceramic vase','精致点缀','边桌或后景'),('装饰画','framed wall art','完善背景','人物头部避开画框线'),
 ('窗帘','soft curtains','柔化窗光','背景窗面'),('边柜','low sideboard','承载小道具','后景横向')],
'咖啡店': [
 ('咖啡桌','small cafe table','轻社交','人物前方'),('木椅','wooden cafe chair','自然、温和','桌边'),
 ('咖啡杯','coffee cup and saucer','明确场景','手边或桌面'),('甜点盘','dessert plate','生活方式细节','与杯子错位'),
 ('菜单','printed menu','叙事与动作','手持或桌边'),('笔记本电脑','laptop in cafe','远程工作','桌面主道具'),
 ('报纸','folded newspaper','慢生活、复古','桌角'),('小花束','small flower vase','柔化桌面','不遮脸'),
 ('吊灯','pendant light','空间识别','上方背景'),('临窗座位','window seat','自然侧光','人物侧后方'),
 ('吧台','coffee counter','行业氛围','远景'),('室内绿植','indoor plant','层次与生机','边缘/后景')],
'街道': [
 ('长椅','street bench','停留、等待','人行道边'),('路灯','street lamp','城市识别','后景竖向'),
 ('隔离柱','street bollard','透视节奏','道路边缘'),('店铺招牌','storefront sign','地点信息','人物头部侧上方'),
 ('公交站牌','bus stop sign','通勤叙事','侧后方'),('自行车','parked bicycle','生活化、动势','边缘半入画'),
 ('雨伞','umbrella','天气与动作','手持或路边'),('橱窗','shop window','反射与城市感','背景平面'),
 ('道路标线','street markings','引导线','地面透视'),('花箱','street planter','软化街景','边缘/中景'),
 ('报刊亭','newsstand','复古城市叙事','后景'),('积水反光','rain puddle reflections','电影感','地面前景')]
}

# Icon drawing (symbolic, not literal photorealism)
def icon(draw, box, kind):
    x0,y0,x1,y1=box; w=x1-x0; h=y1-y0; cx=(x0+x1)/2; cy=(y0+y1)/2
    stroke=COL['navy']; fill='#E8F0F7'; accent=COL['orange']
    def rect(a,b,c,d,**kw): draw.rounded_rectangle((a,b,c,d),radius=8,outline=stroke,width=3,fill=kw.get('fill',fill))
    k=kind
    # generic based on keywords
    if any(s in k for s in ['桌','边柜','吧台','报刊亭']):
        rect(x0+w*.18,y0+h*.35,x1-w*.18,y0+h*.56); draw.line((x0+w*.28,y0+h*.56,x0+w*.25,y1-h*.12),fill=stroke,width=5); draw.line((x1-w*.28,y0+h*.56,x1-w*.25,y1-h*.12),fill=stroke,width=5)
    elif any(s in k for s in ['椅','沙发','长椅']):
        rect(x0+w*.20,y0+h*.35,x1-w*.20,y0+h*.66); draw.line((x0+w*.25,y0+h*.66,x0+w*.22,y1-h*.10),fill=stroke,width=5); draw.line((x1-w*.25,y0+h*.66,x1-w*.22,y1-h*.10),fill=stroke,width=5); draw.line((x0+w*.20,y0+h*.36,x0+w*.16,y0+h*.18),fill=stroke,width=6)
    elif any(s in k for s in ['电脑','显示器']):
        rect(x0+w*.18,y0+h*.18,x1-w*.18,y0+h*.62,fill='#EEF5FB'); draw.line((cx,y0+h*.62,cx,y0+h*.78),fill=stroke,width=5); draw.line((x0+w*.34,y0+h*.79,x1-w*.34,y0+h*.79),fill=stroke,width=5)
    elif any(s in k for s in ['记事本','书籍','菜单','报纸']):
        rect(x0+w*.24,y0+h*.15,x1-w*.24,y1-h*.15,fill='#FFF9EC'); draw.line((x0+w*.34,y0+h*.28,x1-w*.34,y0+h*.28),fill=accent,width=4); draw.line((x0+w*.34,y0+h*.42,x1-w*.34,y0+h*.42),fill=stroke,width=3); draw.line((x0+w*.34,y0+h*.54,x1-w*.34,y0+h*.54),fill=stroke,width=3)
    elif any(s in k for s in ['杯']):
        rect(x0+w*.28,y0+h*.28,x1-w*.34,y0+h*.68,fill='#FFF9EC'); draw.arc((x1-w*.42,y0+h*.36,x1-w*.16,y0+h*.62),-80,80,fill=stroke,width=4); draw.arc((x0+w*.32,y0+h*.03,x0+w*.48,y0+h*.34),180,355,fill=accent,width=4)
    elif any(s in k for s in ['灯']):
        draw.line((cx,y0+h*.18,cx,y1-h*.16),fill=stroke,width=6); draw.polygon([(cx-w*.20,y0+h*.42),(cx+w*.20,y0+h*.42),(cx+w*.10,y0+h*.58),(cx-w*.10,y0+h*.58)],fill='#FFF1C7',outline=stroke); draw.ellipse((cx-w*.10,y1-h*.22,cx+w*.10,y1-h*.10),fill=fill,outline=stroke,width=3)
    elif any(s in k for s in ['绿植','花','花箱']):
        rect(cx-w*.14,y0+h*.60,cx+w*.14,y1-h*.10,fill='#F6E5D0');
        for dx,dy in [(-.12,.46),(.10,.42),(-.04,.32),(.02,.53)]: draw.ellipse((cx+w*dx-w*.10,y0+h*dy-h*.10,cx+w*dx+w*.10,y0+h*dy+h*.10),fill='#A9CDB2',outline=stroke,width=2)
    elif any(s in k for s in ['窗','隔断','橱窗']):
        rect(x0+w*.18,y0+h*.14,x1-w*.18,y1-h*.12,fill='#EAF6FB'); draw.line((cx,y0+h*.14,cx,y1-h*.12),fill=stroke,width=3); draw.line((x0+w*.18,cy,x1-w*.18,cy),fill=stroke,width=3)
    elif any(s in k for s in ['地毯','盖毯','靠垫']):
        rect(x0+w*.22,y0+h*.28,x1-w*.22,y0+h*.72,fill='#F1E7DA');
        for i in range(4): draw.line((x0+w*(.28+i*.12),y0+h*.32,x0+w*(.36+i*.12),y0+h*.68),fill=accent,width=2)
    elif '笔' in k:
        draw.line((x0+w*.26,y1-h*.22,x1-w*.24,y0+h*.20),fill=stroke,width=10); draw.polygon([(x1-w*.24,y0+h*.20),(x1-w*.18,y0+h*.16),(x1-w*.20,y0+h*.26)],fill=accent)
    elif any(s in k for s in ['隔离柱','站牌','招牌']):
        draw.line((cx,y0+h*.24,cx,y1-h*.12),fill=stroke,width=7); rect(cx-w*.20,y0+h*.12,cx+w*.20,y0+h*.42,fill='#FFF1C7'); draw.line((cx-w*.14,y0+h*.26,cx+w*.14,y0+h*.26),fill=accent,width=4)
    elif '自行车' in k:
        r=w*.15; draw.ellipse((x0+w*.18,cy-r,x0+w*.18+2*r,cy+r),outline=stroke,width=4); draw.ellipse((x1-w*.48,cy-r,x1-w*.18,cy+r),outline=stroke,width=4); draw.line((x0+w*.33,cy,x0+w*.50,y0+h*.35,x1-w*.33,cy,x0+w*.33,cy),fill=stroke,width=4)
    elif '伞' in k:
        draw.arc((x0+w*.20,y0+h*.16,x1-w*.20,y0+h*.64),180,360,fill=accent,width=7); draw.line((cx,y0+h*.40,cx,y1-h*.18),fill=stroke,width=5); draw.arc((cx-w*.02,y1-h*.28,cx+w*.18,y1-h*.08),0,120,fill=stroke,width=4)
    elif any(s in k for s in ['道路标线','积水']):
        for i in range(3): draw.line((x0+w*.20+i*w*.20,y0+h*.20,x0+w*.28+i*w*.20,y1-h*.18),fill=accent if '标线' in k else COL['blue2'],width=9)
    else:
        draw.ellipse((x0+w*.25,y0+h*.24,x1-w*.25,y1-h*.20),fill=fill,outline=stroke,width=4)

def make_prop_sheet(category, items):
    W,H=1800,1320
    im=Image.new('RGB',(W,H),COL['white']); d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,120),fill=COL['navy'])
    d.text((58,26),f'{category}场景｜独立道具选择器',font=font(50,True),fill=COL['white'])
    d.text((W-440,42),'道具 ≠ 场景氛围',font=font(28),fill='#DCE6F0')
    cols,rows=4,3; gap=22; margin=48; top=158
    cw=(W-2*margin-(cols-1)*gap)//cols; ch=(H-top-90-(rows-1)*gap)//rows
    for i,(name,en,effect,place) in enumerate(items):
        r,c=divmod(i,cols); x=margin+c*(cw+gap); y=top+r*(ch+gap)
        d.rounded_rectangle((x,y,x+cw,y+ch),radius=20,fill=COL['light'],outline=COL['grid'],width=3)
        d.rounded_rectangle((x+16,y+16,x+135,y+135),radius=16,fill=COL['white'],outline=COL['grid'])
        icon(d,(x+24,y+24,x+127,y+127),name)
        d.text((x+155,y+20),f'{i+1:02d}  {name}',font=font(31,True),fill=COL['navy'])
        draw_wrapped(d,(x+155,y+66),en,font(22),COL['blue'],cw-178,line_gap=3,max_lines=2)
        d.line((x+18,y+150,x+cw-18,y+150),fill=COL['grid'],width=1)
        d.text((x+22,y+170),'视觉作用',font=font(22,True),fill=COL['orange'])
        draw_wrapped(d,(x+125,y+168),effect,font(22),COL['text'],cw-150,line_gap=3,max_lines=2)
        d.text((x+22,y+230),'推荐位置',font=font(22,True),fill=COL['green'])
        draw_wrapped(d,(x+125,y+228),place,font(22),COL['text'],cw-150,line_gap=3,max_lines=2)
    d.text((55,H-58),'使用规则：先选 1 个主道具 + 2–4 个辅助道具；人物交互道具最多 1–2 个，避免“道具堆满但没有叙事”。',font=font(27,True),fill=COL['navy'])
    p=PROP_SEL/f'{category}场景-道具选择器.png'; im.save(p,optimize=True); return p

prop_paths=[make_prop_sheet(k,v) for k,v in props.items()]
prop_index=PROP/'道具与交互-视觉索引-v01.jpg'
contact_sheet(prop_paths,prop_index,'05-道具与交互｜办公・居家・咖啡店・街道',cols=2,thumb=(760,555))

# Main material visual index v2. Archive old file once.
old_index=LIB/'公共资产库-视觉索引-v01.jpg'
archive_old=ARCH/'素材图库-视觉索引-v01.jpg'
if old_index.exists() and not archive_old.exists():
    shutil.copy2(old_index,archive_old)
# use original existing as first thumbnail then new indexes + scene source
scene_img=ROOT/'03-专项生产库/丝袜效果图/04-生产资产/展示方式/D02-生活方式构图-v02.png'
thumbs=[]
if archive_old.exists(): thumbs.append(archive_old)
thumbs.extend([stand_index,prop_index])
if scene_img.exists(): thumbs.append(scene_img)
contact_sheet(thumbs,old_index,'素材图库｜可复用视觉变量索引 v2',cols=2,thumb=(760,500))

# Save structured data
(STAND_DATA/'人物站位参数库.json').write_text(json.dumps({'version':'1.0','updated':'2026-08-05','cards':stand_specs},ensure_ascii=False,indent=2),encoding='utf-8')
(PROP_DATA/'场景道具选择器.json').write_text(json.dumps({'version':'1.0','updated':'2026-08-05','categories':{k:[{'name':a,'prompt':b,'effect':c,'placement':d} for a,b,c,d in v] for k,v in props.items()}},ensure_ascii=False,indent=2),encoding='utf-8')

print('generated',len(stand_paths),'stand cards,',len(prop_paths),'prop sheets')
