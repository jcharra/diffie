export default async function getImageUrlForWord(word: string) {
  return `https://charra-diffie.s3.eu-central-1.amazonaws.com/${word}.jpg`;
}