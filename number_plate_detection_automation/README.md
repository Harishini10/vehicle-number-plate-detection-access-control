# Week 2: Automated Number Plate Text Extraction

### 📘 Objective
Build a Python-based automation pipeline to detect and extract vehicle registration numbers from images using **OpenCV** for image preprocessing and **Tesseract OCR** for optical character recognition.

---

### ⚙️ Steps
1. Place all vehicle images (`.png`, `.jpg`) inside the `dataset/` folder.  
2. Run the main program:
   ```bash
   python main.py
3. Preprocessed images are automatically saved inside the **`processed_images/`** folder.
4. Extracted text results (number plates) are logged into **`entry_log.csv`** and displayed in the terminal.

---

### 🧩 Tools & Libraries
- **OpenCV** → Image reading, resizing, grayscaling, denoising.  
- **Pytesseract (Tesseract OCR)** → Extracts text from number plate regions.  

---

### 📁 Output Files
- **`processed_images/`** → Contains all preprocessed grayscale and enhanced images.  
- **`entry_log.csv`** → Stores the extracted text (number plate values) for each image.  
- **Console Summary** → Displays detected text and preprocessing results for each image.
