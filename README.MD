# Image Resizer Tool 🖼️

A simple Python tool to resize all images in a folder to a fixed size using the Pillow library.

---

## 🛠  Requirements:

-Python 3.x
-Pillow 

---

## ✅ Features:
- Automatically resizes `.jpg`, `.jpeg`, and `.png` images
- Saves resized images into a separate `output/` folder
- Renames output images like: `resized_image_1.jpg`, `resized_image_2.png`, etc.
- Uses a fixed size of `800x600` pixels

---

## 📂 Folder Structure

Image_Resizer_Tool/
│
├── Images/
│ ├── image1.jpg
│ ├── image2.png
│ ├── ...
│ └── output/
│ ├── resized_image_1.jpg
│ └── resized_image_2.png
│
├── resizer.py
└── README.md

---

## ▶️ How to Run

1. Install Pillow if you don’t have it:
   ```bash
   pip install pillow

2. Run the script:

    ```bash
    python resizer.py

---

## 📸 Sample Output

Resized: image1.jpg
Resized: image2.png
Resized images saved in Images/output/