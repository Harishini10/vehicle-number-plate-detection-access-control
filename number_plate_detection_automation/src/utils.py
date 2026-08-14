import cv2

def save_annotated_image(image, bbox, text, output_path):
    x, y, w, h = bbox

    # Draw bounding box
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Add OCR text
    cv2.putText(image, text, (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2)

    cv2.imwrite(output_path, image)
