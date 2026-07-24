import { AbsoluteFill, Sequence, useVideoConfig } from "remotion";
import { LogoIntro } from "./segments/LogoIntro";
import { DataAnimations } from "./segments/DataAnimations";
import { ProductFeatures } from "./segments/ProductFeatures";
import { Testimonials } from "./segments/Testimonials";
import { CTA } from "./segments/CTA";

export const ProductLaunch: React.FC<{
  companyName: string;
  logoText: string;
  slogan: string;
  primaryColor: string;
  accentColor: string;
}> = ({ companyName, logoText, slogan, primaryColor, accentColor }) => {
  return (
    <AbsoluteFill style={{ backgroundColor: primaryColor }}>
      <Sequence from={0} durationInFrames={150}>
        <LogoIntro logoText={logoText} accentColor={accentColor} />
      </Sequence>
      <Sequence from={150} durationInFrames={450}>
        <DataAnimations companyName={companyName} accentColor={accentColor} />
      </Sequence>
      <Sequence from={600} durationInFrames={750}>
        <ProductFeatures accentColor={accentColor} />
      </Sequence>
      <Sequence from={1350} durationInFrames={300}>
        <Testimonials accentColor={accentColor} />
      </Sequence>
      <Sequence from={1650} durationInFrames={150}>
        <CTA companyName={companyName} slogan={slogan} accentColor={accentColor} />
      </Sequence>
    </AbsoluteFill>
  );
};