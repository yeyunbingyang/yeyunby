import { Composition } from "remotion";
import { ProductLaunch } from "./ProductLaunch";

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="ProductLaunch"
      component={ProductLaunch}
      durationInFrames={1800}
      fps={30}
      width={1920}
      height={1080}
      defaultProps={{
        companyName: "您的公司",
        logoText: "LOGO",
        slogan: "让未来触手可及",
        primaryColor: "#0A1628",
        accentColor: "#00D4FF",
      }}
    />
  );
};
