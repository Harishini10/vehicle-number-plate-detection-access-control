# src/preprocessor.py
import cv2
import numpy as np

def preprocess_plate(plate_img):
    """
    Preprocess the cropped plate image for OCR:
    - convert to gray
    - resize (scale up)
    - denoise and adaptive threshold
    Returns processed grayscale image suitable for pytesseract.
    """
    gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
    # enlarge to improve OCR
    h, w = gray.shape
    factor = 2
    gray = cv2.resize(gray, (w*factor, h*factor), interpolation=cv2.INTER_CUBIC)
    # denoise
    gray = cv2.bilateralFilter(gray, 9, 75, 75)
    # adaptive threshold
    th = cv2.adaptiveThreshold(gray, 255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 31, 9)
    return th
