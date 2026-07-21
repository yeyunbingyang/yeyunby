import { AbsoluteFill, useCurrentFrame, spring, interpolate } from "remotion";
var features = [
  { title: '智能分析引擎', desc: 'AI 驱动的实时洞察', icon: '📊' },
  { title: '全渠道连接', desc: '一键接入 50+ 数据源', icon: '🔗' },
  { title: '自动化工作流', desc: '零代码搭建流程', icon: '⚡' },
  { title: '实时协作平台', desc: '团队同步零延迟', icon: '🤝' },
  { title: '安全合规', desc: '企业级数据安全', icon: '🔒' },
  { title: '智能预测', desc: 'ML 趋势预判', icon: '🎯' },
];
export const ProductFeatures: React.FC<{ accentColor: string }> = ({ accentColor }) => {
  var f = useCurrentFrame();
  return (
    <AbsoluteFill>
      <div style={{ fontSize: 38, fontWeight: 800, color: 'white', textAlign: 'center', marginTop: 40, opacity: interpolate(f, [0, 30], [0, 1]) }}>核心功能</div>
      {features.map((ft, i) => {
        var lf = f - i * 125;
        var appear = spring({ frame: lf, fps: 30, config: { mass: 0.8, damping: 12 } });
        var ry = interpolate(appear, [0, 1], [90, 0]);
        var op = interpolate(lf, [0, 30], [0, 1]);
        return (
          <div key={i} style={{ position: 'absolute', left: 100 + (i % 3) * 580, top: 100 + Math.floor(i / 3) * 350, width: 500, height: 280, transform: 'perspective(1000px) rotateY(' + ry + 'deg)', opacity: op,
            background: 'linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.03))', border: '1px solid ' + (lf > 0 ? accentColor : 'transparent'), borderRadius: 24, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 16 }}>
            <div style={{ fontSize: 48 }}>{ft.icon}</div>
            <div style={{ fontSize: 26, fontWeight: 700, color: 'white' }}>{ft.title}</div>
            <div style={{ fontSize: 16, color: 'rgba(255,255,255,0.6)' }}>{ft.desc}</div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};