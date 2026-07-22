import { AbsoluteFill, useCurrentFrame, interpolate, spring, useVideoConfig } from "remotion";

interface Props { accentColor: string; }

const testimonials = [
  { text: "这款产品彻底改变了我们的数据分析流程", author: "张三 · 科技公司CTO", role: "效率提升 300%" },
  { text: "部署简单，效果立竿见影，团队爱不释手", author: "李四 · 电商VP", role: "营收增长 180%" },
  { text: "AI 预测的准确率远超我们的预期", author: "王五 · 金融分析师", role: "准确率 94%" },
  { text: "客户支持团队的使用率达到了 100%", author: "赵六 · 运营总监", role: "全员使用中" },
  { text: "从决策到落地，比之前快了整整 5 倍", author: "陈七 · 产品负责人", role: "交付周期 -80%" },
];

const TestimonialCard: React.FC<{ t: typeof testimonials[0]; index: number; frame: number; accentColor: string }> =
  ({ t, index, frame, accentColor }) => {
    const cardDuration = 60;
    const localFrame = frame - index * cardDuration;
    const slideIn = spring({ frame: localFrame, fps: 30, config: { damping: 14 } });
    const opacity = interpolate(localFrame, [0, 15, cardDuration - 15, cardDuration], [0, 1, 1, 0]);
    const x = interpolate(slideIn, [0, 1], [200, 0]);

    return (
      <div style={{
        position: 'absolute', left: 160, top: 120, width: 1600, height: 700,
        transform: `translateX(${x}px)`, opacity,
        display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 20
      }}>
        <div style={{ fontSize: 72, color: accentColor, opacity: 0.3 }}>"</div>
        <div style={{ fontSize: 32, color: 'white', textAlign: 'center', maxWidth: 1200, lineHeight: 1.6, fontStyle: 'italic' }}>
          {t.text}
        </div>
        <div style={{ width: 60, height: 2, backgroundColor: accentColor, opacity: 0.5, margin: '10px 0' }} />
        <div style={{ fontSize: 18, color: 'rgba(255,255,255,0.7)' }}>{t.author}</div>
        <div style={{ fontSize: 14, color: accentColor, marginTop: 4 }}>{t.role}</div>
      </div>
    );
  };

export const Testimonials: React.FC<Props> = ({ accentColor }) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ backgroundColor: 'rgba(10,22,40,0.95)' }}>
      <div style={{ fontSize: 36, fontWeight: 800, color: 'white', textAlign: 'center', marginTop: 40 }}>
        客户怎么说
      </div>
      {testimonials.map((t, i) => (
        <TestimonialCard key={i} t={t} index={i} frame={frame} accentColor={accentColor} />
      ))}
    </AbsoluteFill>
  );
};