import { AbsoluteFill, useCurrentFrame, spring, interpolate } from "remotion";
var tdata = [
  { text: '彻底改变了我们的数据分析流程', author: '张三 · CTO', role: '效率+300%' },
  { text: '部署简单，效果立竿见影', author: '李四 · VP', role: '营收+180%' },
  { text: 'AI 预测准确率远超预期', author: '王五 · 分析师', role: '准确率94%' },
  { text: '团队使用率达到了 100%', author: '赵六 · 总监', role: '全员使用' },
  { text: '比之前快了整整 5 倍', author: '陈七 · PM', role: '交付-80%' },
];
export const Testimonials: React.FC<{ accentColor: string }> = ({ accentColor }) => {
  var f = useCurrentFrame();
  return (
    <AbsoluteFill style={{ background: '#0A1628' }}>
      <div style={{ fontSize: 36, fontWeight: 800, color: 'white', textAlign: 'center', marginTop: 40 }}>客户怎么说</div>
      {tdata.map((t, i) => {
        var lf = f - i * 60;
        var si = spring({ frame: lf, fps: 30, config: { damping: 14 } });
        var op = interpolate(lf, [0, 15, 45, 60], [0, 1, 1, 0]);
        return (
          <div key={i} style={{ position: 'absolute', left: 160, top: 120, width: 1600, height: 700, transform: 'translateX(' + interpolate(si, [0, 1], [200, 0]) + 'px)', opacity: op, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 20 }}>
            <div style={{ fontSize: 72, color: accentColor, opacity: 0.3 }}>"</div>
            <div style={{ fontSize: 32, color: 'white', textAlign: 'center', maxWidth: 1200, fontStyle: 'italic' }}>{t.text}</div>
            <div style={{ width: 60, height: 2, background: accentColor, opacity: 0.5 }} />
            <div style={{ fontSize: 18, color: 'rgba(255,255,255,0.7)' }}>{t.author}</div>
            <div style={{ fontSize: 14, color: accentColor }}>{t.role}</div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};