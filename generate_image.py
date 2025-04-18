import os
from io import BytesIO
import requests
from PIL import Image
from openai import OpenAI

from pathlib import Path

script_dir = Path(__file__).resolve().parent

key = open("OPENAI_KEY").readline().strip()
client = OpenAI(api_key=key)

prompt_setup = """
Du bist ein Comiczeichner, der einfache, fast schon ikonographische Bilder zeichnet.
Du verwendest sepiaartige Farben und sanfte zeichnungen.
Niemals darf in den Bildern Text erscheinen.
"""


def get_detailed_prompt(prompt):
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": prompt_setup},
            {"role": "user",
             "content": f"Zeichne nun folgenden Begriff: {prompt}"}
        ]).choices[0].message.content


def generate_image_for_term(term):
    filename = os.path.join(script_dir, "raw_images", term.lower() + ".jpg")
    if os.path.exists(filename):
        print(f"File {filename} already exists!")
        return

    detailed_prompt = get_detailed_prompt(term)
    print(f"Generating {filename} with detailed prompt: \n{detailed_prompt}")
    response = client.images.generate(
        model="dall-e-3",
        prompt=detailed_prompt,
        n=1,
        size="1024x1024"
    )

    # Get image URL from the response
    image_url = response.data[0].url

    # Download the image
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))

    # Resize to 512x512
    image_resized = image.resize((512, 512), Image.Resampling.LANCZOS)

    # Save or display
    image_resized.save(filename)
    print(f"Image for {term} successfully generated!")


while True:
    word = input("Begriff: ")
    if not word:
        break
    generate_image_for_term(word)
