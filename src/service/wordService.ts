import {PAIRS} from "./pairs";

export async function getRandomWordList(length: number): Promise<[string, string][]> {
  const list: [string, string][] = [];

  let c = 0;
  while (list.length < length) {
    const pair = PAIRS[Math.floor(PAIRS.length * Math.random())];
    if (list.indexOf(pair) === -1) {
      list.push(pair);
    }
    c++;
    if (c > 1000) {
      console.error("Too many attempts");
      break;
    }
  }
  return Promise.resolve(list);
}
