import pytesseract
import cv2


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def read_plate_text(plate_image):
    if plate_image is None:
        return ""

    # Convert to grayscale
    gray = cv2.cvtColor(plate_image, cv2.COLOR_BGR2GRAY)

    # Light blur to reduce noise
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # Binary thresholding
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    # OCR config
    config = "--psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # Running OCR
    text = pytesseract.image_to_string(thresh, config=config)

    # Clean text
    text = text.strip().replace(" ", "").replace("\n", "")

    return text
