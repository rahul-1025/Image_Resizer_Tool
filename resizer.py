import os
from PIL import Image

folder_path = "C:/Users/saine/OneDrive/Desktop/BroskiesHub/Image_Resizer_Tool/Images"

output_folder = os.path.join(folder_path, "output")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

new_size = (800, 600)

count = 1

for file_name in os.listdir(folder_path):
    if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(folder_path, file_name)
        img = Image.open(image_path)
        img = img.resize(new_size)

        ext = os.path.splitext(file_name)[1]
        output_name = f"resized_image_{count}{ext}"
        output_path = os.path.join(output_folder, output_name)

        img.save(output_path)
        print(f"Saved: {output_name}")
        count += 1
