import cv2
import os

CASCADE_PATH = os.path.join("haarcascades", "haarcascade_russian_plate_number.xml")

def detect_plate_in_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None, None, None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plate_cascade = cv2.CascadeClassifier(CASCADE_PATH)

    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(60,20))

    if len(plates) == 0:
        return img, None, None

    plates = sorted(plates, key=lambda x: x[2]*x[3], reverse=True)
    x, y, w, h = plates[0]
    plate_img = img[y:y+h, x:x+w]
    return img, plate_img, (x, y, w, h)
