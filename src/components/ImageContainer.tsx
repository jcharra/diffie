import { useEffect, useState } from "react";
import getImageUrlForWord from "../service/imageService";

export default function ImageContainer({ word }: { word: string }) {
  const [url, setUrl] = useState<string>("");

  useEffect(() => {
    getImageUrlForWord(word)
      .then(url => {
        setUrl(url);
      });
  }, [word]);

  return <>
    <img src={url} alt={word} width="300px" />
  </>;
}