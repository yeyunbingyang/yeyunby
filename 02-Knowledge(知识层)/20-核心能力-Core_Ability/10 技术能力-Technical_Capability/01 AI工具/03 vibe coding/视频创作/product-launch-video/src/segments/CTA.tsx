import { AbsoluteFill, useCurrentFrame, interpolate, spring, useVideoConfig } from "remotion";

interface Props { companyName: string; slogan: string; accentColor: string; }

export const CTA: React.FC<Props> = ({ companyName, slogan, accentColor }) => {
  const frame = useCurrentFrame();
  const scale = spring({ frame, fps: 30, config: { mass: 0.6, damping: 10 } });
  const opacity = interpolate(frame, [0, 20, 120, 150], [0, 1, 1, 0]);
  const countdownOpacity = interpolate(frame, [0, 90, 120, 150], [1, 1, 0.5, 0]);

  const countdown = Math.max(0, Math.ceil((150 - frame) / 30));
  const ctaScale = spring({ frame: frame - 120, fps: 30, config: { mass: 0.4, damping: 8 } });

  return (
    <AbsoluteFill style={{
      display: 'flex', alignItems: 'center', justifyContent: 'center',
      background: `radial-gradient(circle at center, ${accentColor}15 0%, #0A1628 70%)`
    }}>
      <div style={{
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 30,
        transform: `scale(${scale})`, opacity
      }}>
        <div style={{ fontSize: 60, fontWeight: 300, color: 'white', letterSpacing: 12, opacity: interpolate(frame, [0, 60], [0, 1]) }}>
          {companyName}
        </div>
        <div style={{ fontSize: 48, fontWeight: 800, color: accentColor, textShadow: `0 0 40px ${accentColor}` }}>
          {slogan}
        </div>
        <div style={{
          fontSize: 24, color: 'white', opacity: interpolate(frame, [60, 120], [0, 1]),
          padding: '16px 48px', border: '2px solid ' + accentColor, borderRadius: 50,
          cursor: 'pointer', letterSpacing: 4
        }}>
          立即体验
        </div>

        <div style={{
          position: 'absolute', top: -60, fontSize: 120, fontWeight: 900, color: 'white',
          opacity: countdownOpacity, transform: `scale(${ctaScale})`,
          textShadow: `0 0 60px ${accentColor}`
        }}>
          {countdown > 0 ? countdown : ''}
        </div>

        <div style={{
          position: 'absolute', bottom: -100, fontSize: 14, color: 'rgba(255,255,255,0.3)',
          letterSpacing: 2
        }}>
          © 2026 {companyName}. All rights reserved.
        </div>
      </div>
    </AbsoluteFill>
  );
};