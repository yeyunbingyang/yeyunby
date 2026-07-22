import { AbsoluteFill, useCurrentFrame, spring, interpolate } from "remotion";
export const DataAnimations: React.FC<{ companyName: string; accentColor: string }> = ({ companyName, accentColor }) => {
  var f = useCurrentFrame();
  var bars = [{ h: 90, l: '用户增长', v: '2.5M' }, { h: 75, l: '营收增长', v: '180%' }, { h: 60, l: '覆盖城市', v: '50+' }, { h: 85, l: '满意度', v: '98%' }];
  var section = Math.floor(f / 150);
  return (
    <AbsoluteFill style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ fontSize: 42, fontWeight: 800, color: 'white', marginBottom: 60, opacity: interpolate(f, [0, 30], [0, 1]) }}>{companyName}</div>
      {section === 0 && (
        <div style={{ display: 'flex', gap: 60 }}>
          {bars.map((b, i) => {
            var grow = spring({ frame: f - i * 15, fps: 30, config: { damping: 15 } });
            return (
              <div key={i} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 8, width: 160 }}>
                <div style={{ color: 'white', fontSize: 18, fontWeight: 700 }}>{b.v}</div>
                <div style={{ width: 60, height: 200, background: 'rgba(255,255,255,0.1)', borderRadius: 8, overflow: 'hidden' }}>
                  <div style={{ position: 'absolute', bottom: 0, width: 60, height: b.h * grow + '%', background: accentColor, borderRadius: 8 }} />
                </div>
                <div style={{ color: 'rgba(255,255,255,0.7)', fontSize: 14 }}>{b.l}</div>
              </div>
            );
          })}
        </div>
      )}
      {section === 1 && <div style={{ fontSize: 24, color: 'white' }}>增长曲线图</div>}
      {section === 2 && <div style={{ fontSize: 24, color: 'white' }}>城市覆盖地图</div>}
    </AbsoluteFill>
  );
};