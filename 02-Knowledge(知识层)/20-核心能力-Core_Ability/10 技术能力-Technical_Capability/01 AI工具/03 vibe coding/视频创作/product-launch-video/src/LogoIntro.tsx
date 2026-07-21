import { AbsoluteFill, useCurrentFrame, interpolate, spring } from "remotion";
export const LogoIntro: React.FC<{ logoText: string; accentColor: string }> = ({ logoText, accentColor }) => {
  var f = useCurrentFrame();
  var s = spring({ frame: f, fps: 30, config: { mass: 0.5, damping: 10 } });
  var g = interpolate(f, [0, 30, 100, 150], [0, 1, 0.8, 0]);
  return (
    <AbsoluteFill style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'radial-gradient(circle, rgba(0,212,255,0.1) 0%, #0A1628 100%)' }}>
      <div style={{ fontSize: 80, fontWeight: 900, color: 'white', transform: 'scale('+s+')', textShadow: '0 0 40px '+accentColor+', 0 0 80px '+accentColor, opacity: g }}>
        {logoText}
      </div>
      <div style={{ position: 'absolute', bottom: '30%', fontSize: 24, color: accentColor, opacity: interpolate(f, [100, 150], [0, 1]) }}>
        PRODUCT LAUNCH
      </div>
    </AbsoluteFill>
  );
};