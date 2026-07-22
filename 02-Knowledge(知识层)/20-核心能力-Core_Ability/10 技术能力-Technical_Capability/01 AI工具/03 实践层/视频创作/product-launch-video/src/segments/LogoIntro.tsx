import { AbsoluteFill, useCurrentFrame, interpolate, spring, useVideoConfig } from "remotion";

interface Props { logoText: string; accentColor: string; }

const Particle = ({ delay, x, y, color, frame }: { delay: number; x: number; y: number; color: string; frame: number }) => {
  const progress = spring({ frame: frame - delay, fps: 30, config: { damping: 12 } });
  const opacity = interpolate(frame - delay, [0, 20, 120, 150], [0, 1, 1, 0]);
  return (
    <div style={{
      position: 'absolute', left: x, top: y, width: 4, height: 4, borderRadius: '50%',
      backgroundColor: color, opacity, transform: `translate(${progress * 200 - 100}px, ${progress * 150 - 75}px) scale(${progress})`,
      boxShadow: `0 0 6px ${color}`
    }} />
  );
};

export const LogoIntro: React.FC<Props> = ({ logoText, accentColor }) => {
  const frame = useCurrentFrame();
  const logoScale = spring({ frame, fps: 30, config: { mass: 0.5, damping: 10 } });
  const glowOpacity = interpolate(frame, [0, 30, 100, 150], [0, 1, 0.8, 0]);
  const particles = Array.from({ length: 40 }, (_, i) => ({
    delay: i * 3, x: 960 + Math.cos(i * 1.2) * 80, y: 540 + Math.sin(i * 0.8) * 60, color: accentColor
  }));

  return (
    <AbsoluteFill style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      {particles.map((p, i) => <Particle key={i} {...p} frame={frame} />)}
      <div style={{
        fontSize: 80, fontWeight: 900, color: 'white', letterSpacing: 8,
        transform: `scale(${logoScale})`, textShadow: `0 0 40px ${accentColor}, 0 0 80px ${accentColor}`,
        opacity: glowOpacity
      }}>
        {logoText}
      </div>
      <div style={{
        position: 'absolute', bottom: '30%', fontSize: 24, color: accentColor, letterSpacing: 4,
        opacity: interpolate(frame, [100, 150], [0, 1])
      }}>
        PRODUCT LAUNCH
      </div>
    </AbsoluteFill>
  );
};