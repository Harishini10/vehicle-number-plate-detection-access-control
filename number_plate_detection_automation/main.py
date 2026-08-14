import os
import cv2
from src.detector import detect_plate_in_image
from src.ocr_engine import read_plate_text
from src.access_control import check_access
from src.utils import save_annotated_image

INPUT_DIR = "dataset"
OUTPUT_DIR = "output"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def process_images():
    print("\n=== Processing Images ===\n")
    
    for img_name in os.listdir(INPUT_DIR):
        img_path = os.path.join(INPUT_DIR, img_name)

        if not img_path.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        print(f"\nProcessing: {img_name}")

        # 1. Detect Plate
        original_img, plate_img, bbox = detect_plate_in_image(img_path)

        if plate_img is None:
            print("⚠ No number plate detected.")
            continue

        # 2. OCR - Read Text
        plate_text = read_plate_text(plate_img)
        print("Extracted Text:", plate_text)

        # 3. Access Control
        status = check_access(plate_text)
        print("Access:", status)

        # 4. Save Annotated Output
        save_path = os.path.join(OUTPUT_DIR, img_name)
        save_annotated_image(original_img, bbox, plate_text, save_path)

    print("\n=== Processing Completed ===")

if __name__ == "__main__":
    process_images()
