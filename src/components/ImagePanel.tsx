import ImageContainer from "./ImageContainer";

export function ImagePanel({ word1, word2 }: { word1: string, word2: string }) {
  return <div className="splitPane">
    <div className="image left">
      <ImageContainer word={word1} />
    </div>
    <div className="image right">
      <ImageContainer word={word2} />
    </div>
  </div>;
}