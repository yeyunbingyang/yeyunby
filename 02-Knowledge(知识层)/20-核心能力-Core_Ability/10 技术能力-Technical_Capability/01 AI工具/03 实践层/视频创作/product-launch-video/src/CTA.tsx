import { AbsoluteFill, useCurrentFrame, spring, interpolate } from "remotion";
export const CTA: React.FC<{ companyName: string; slogan: string; accentColor: string }> = ({ companyName, slogan, accentColor }) => {
  var f = useCurrentFrame();
  var s = spring({ frame: f, fps: 30, config: { mass: 0.6, damping: 10 } });
  return (
    <AbsoluteFill style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'radial-gradient(circle at center, ' + accentColor + '15, #0A1628 70%)' }}>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 30, transform: 'scale(' + s + ')', opacity: interpolate(f, [0, 20, 120, 150], [0, 1, 1, 0]) }}>
        <div style={{ fontSize: 60, fontWeight: 300, color: 'white', letterSpacing: 12, opacity: interpolate(f, [0, 60], [0, 1]) }}>{companyName}</div>
        <div style={{ fontSize: 48, fontWeight: 800, color: accentColor, textShadow: '0 0 40px ' + accentColor }}>{slogan}</div>
        <div style={{ fontSize: 24, color: 'white', opacity: interpolate(f, [60, 120], [0, 1]), padding: '16px 48px', border: '2px solid ' + accentColor, borderRadius: 50, letterSpacing: 4 }}>立即体验</div>
      </div>
    </AbsoluteFill>
  );
};