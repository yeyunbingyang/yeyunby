import { AbsoluteFill, useCurrentFrame, interpolate, spring, useVideoConfig } from "remotion";

interface Props { accentColor: string; }

const features = [
  { title: "智能分析引擎", desc: "AI 驱动的实时数据洞察", icon: "📊" },
  { title: "全渠道连接", desc: "一键接入 50+ 数据源", icon: "🔗" },
  { title: "自动化工作流", desc: "零代码搭建业务流程", icon: "⚡" },
  { title: "实时协作平台", desc: "团队同步零延迟", icon: "🤝" },
  { title: "安全合规", desc: "企业级数据安全保障", icon: "🔒" },
  { title: "智能预测", desc: "基于 ML 的趋势预判", icon: "🎯" },
];

const FeatureCard3D: React.FC<{ feature: typeof features[0]; index: number; frame: number; accentColor: string }> =
  ({ feature, index, frame, accentColor }) => {
    const localFrame = frame - index * 125;
    const appear = spring({ frame: localFrame, fps: 30, config: { mass: 0.8, damping: 12 } });
    const rotateY = interpolate(appear, [0, 1], [90, 0]);
    const opacity = interpolate(localFrame, [0, 30], [0, 1]);

    return (
      <div style={{
        position: 'absolute',
        left: 100 + (index % 3) * 580,
        top: 100 + Math.floor(index / 3) * 350,
        width: 500, height: 280,
        transform: `perspective(1000px) rotateY(${rotateY}deg)`,
        opacity, transition: 'all 0.3s'
      }}>
        <div style={{
          width: '100%', height: '100%', borderRadius: 24,
          background: 'linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.03) 100%)',
          border: '1px solid ' + (localFrame > 0 ? accentColor : 'transparent'),
          boxShadow: localFrame > 0 ? `0 0 30px rgba(0,212,255,0.2)` : 'none',
          display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 16,
          padding: 24
        }}>
          <div style={{ fontSize: 48 }}>{feature.icon}</div>
          <div style={{ fontSize: 26, fontWeight: 700, color: 'white' }}>{feature.title}</div>
          <div style={{ fontSize: 16, color: 'rgba(255,255,255,0.6)', textAlign: 'center' }}>{feature.desc}</div>
        </div>
      </div>
    );
  };

export const ProductFeatures: React.FC<Props> = ({ accentColor }) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill>
      <div style={{ fontSize: 38, fontWeight: 800, color: 'white', textAlign: 'center', marginTop: 40, opacity: interpolate(frame, [0, 30], [0, 1]) }}>
        核心功能
      </div>
      {features.map((f, i) => (
        <FeatureCard3D key={i} feature={f} index={i} frame={frame} accentColor={accentColor} />
      ))}
    </AbsoluteFill>
  );
};