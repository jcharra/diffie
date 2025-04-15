import { useState, useEffect, useCallback } from "react";
import { getRandomWordList } from "../service/wordService";
import { ImagePanel } from "./ImagePanel";

export default function AppContainer() {
  const [wordList, setWordList] = useState<[string, string][]>();
  const [index, setIndex] = useState(-1);
  const [word1, setWord1] = useState<string>("");
  const [word2, setWord2] = useState<string>("");

  useEffect(() => {
    getRandomWordList(5)
      .then((list) => {
        setWordList(list);
      });
  }, []);

  useEffect(() => {
    if (wordList) {
      setIndex(0);
    }
  }, [wordList]);

  useEffect(() => {
    if (wordList && index > -1) {
      setWord1(wordList[index][0]);
      setWord2(wordList[index][1]);
    }
  }, [index, setWord1, setWord2, wordList]);

  const submit = useCallback(() => {
    setIndex(i => i + 1);
  }, []);

  return <>
    <h1>Diffie #{index + 1} des Tages</h1>
    <ImagePanel word1={word1} word2={word2} />
    <button className="btn" onClick={() => submit()}>Weiter</button>
  </>;

}