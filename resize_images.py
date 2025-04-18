import os
from PIL import Image

# Set the directory containing your images
input_dir = "raw_images"
output_dir = "public"

# Resize dimensions
target_size = (512, 512)

# Supported image extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

for filename in os.listdir(input_dir):
    if filename.lower().endswith(image_extensions):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        try:
            with Image.open(input_path) as img:
                resized_img = img.resize(target_size, Image.ANTIALIAS)
                resized_img.save(output_path)
                print(f"Resized {filename} and saved to {output_path}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
