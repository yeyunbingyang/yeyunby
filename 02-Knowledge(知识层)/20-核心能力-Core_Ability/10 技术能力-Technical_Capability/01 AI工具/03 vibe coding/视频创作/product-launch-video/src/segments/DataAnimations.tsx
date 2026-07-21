import { AbsoluteFill, useCurrentFrame, interpolate, spring, useVideoConfig } from "remotion";

interface Props { companyName: string; accentColor: string; }

const AnimatedBar: React.FC<{ height: number; delay: number; label: string; value: string; accentColor: string; frame: number }> =
  ({ height, delay, label, value, accentColor, frame }) => {
    const grow = spring({ frame: frame - delay, fps: 30, config: { damping: 15 } });
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 8, width: 160 }}>
        <div style={{ color: 'white', fontSize: 18, fontWeight: 700 }}>{value}</div>
        <div style={{ width: 60, height: 200, backgroundColor: 'rgba(255,255,255,0.1)', borderRadius: 8, overflow: 'hidden', position: 'relative' }}>
          <div style={{
            position: 'absolute', bottom: 0, width: '100%', height: `${height * grow}%`,
            backgroundColor: accentColor, borderRadius: 8,
            boxShadow: `0 0 20px ${accentColor}`
          }} />
        </div>
        <div style={{ color: 'rgba(255,255,255,0.7)', fontSize: 14 }}>{label}</div>
      </div>
    );
  };

const AnimatedLine: React.FC<{ frame: number; accentColor: string }> = ({ frame, accentColor }) => {
  const progress = spring({ frame, fps: 30, config: { damping: 20 } });
  const points = [
    [100, 350], [300, 300], [500, 250], [700, 280], [900, 200], [1100, 150], [1300, 180], [1500, 100], [1700, 120], [1820, 80]
  ];
  const drawLen = Math.floor(points.length * progress);
  const pathD = points.slice(0, drawLen).map((p, i) => (i === 0 ? 'M' : 'L') + p[0] + ' ' + p[1]).join(' ');
  return (
    <svg width={1820} height={400} style={{ position: 'absolute', top: 100 }}>
      <path d={pathD} stroke={accentColor} strokeWidth={3} fill="none" strokeLinecap="round" strokeLinejoin="round" />
      {points.slice(0, drawLen).map((p, i) => (
        <circle key={i} cx={p[0]} cy={p[1]} r={6} fill="white" stroke={accentColor} strokeWidth={2}>
          <animate attributeName="r" values="4;8;4" dur="1.5s" repeatCount="indefinite" />
        </circle>
      ))}
    </svg>
  );
};

export const DataAnimations: React.FC<Props> = ({ companyName, accentColor }) => {
  const frame = useCurrentFrame();
  const section = Math.floor(frame / 150);

  return (
    <AbsoluteFill style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ fontSize: 42, fontWeight: 800, color: 'white', marginBottom: 60, opacity: interpolate(frame, [0, 30], [0, 1]) }}>
        {companyName} 的成长轨迹
      </div>

      {section === 0 && (
        <div style={{ display: 'flex', gap: 60 }}>
          <AnimatedBar height={90} delay={0} label="用户增长" value="2.5M" accentColor="#00D4FF" frame={frame} />
          <AnimatedBar height={75} delay={20} label="营收增长" value="180%" accentColor="#00D4FF" frame={frame} />
          <AnimatedBar height={60} delay={40} label="覆盖城市" value="50+" accentColor="#00D4FF" frame={frame} />
          <AnimatedBar height={85} delay={60} label="客户满意度" value="98%" accentColor="#00D4FF" frame={frame} />
        </div>
      )}

      {section === 1 && (
        <div style={{ position: 'relative', width: 1820, height: 400 }}>
          <AnimatedLine frame={frame - 150} accentColor={accentColor} />
          <div style={{ position: 'absolute', bottom: 40, left: 100, fontSize: 14, color: 'rgba(255,255,255,0.5)' }}>
            时间 → (逐月展开曲线)
          </div>
        </div>
      )}

      {section === 2 && (
        <div style={{ position: 'relative', width: 1800, height: 600 }}>
          <div style={{
            position: 'absolute', left: 100, top: 100, width: 500, height: 400,
            backgroundColor: 'rgba(255,255,255,0.05)', borderRadius: 20,
            border: '1px solid ' + accentColor, opacity: interpolate(frame - 300, [0, 30], [0, 1]),
            display: 'flex', alignItems: 'center', justifyContent: 'center'
          }}>
            <div style={{ textAlign: 'center' }}>
              <div style={{ fontSize: 60, color: 'white', fontWeight: 800 }}>50+</div>
              <div style={{ fontSize: 18, color: accentColor, marginTop: 8 }}>覆盖城市</div>
              <div style={{ width: 300, height: 2, backgroundColor: accentColor, margin: '20px auto', opacity: 0.5 }} />
              <div style={{ display: 'flex', gap: 20, justifyContent: 'center' }}>
                {['北京', '上海', '深圳', '杭州'].map(c => (
                  <div key={c} style={{ color: 'rgba(255,255,255,0.7)', fontSize: 14 }}>{c}</div>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};