from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
input_dir = Path(r"C:\Users\sweth\Downloads\haas_berk_assignment")

for img_file in input_dir.rglob("*.png"):
    if "15" in img_file.name:
        print(img_file)

        # Open the image using Pillow
        image = Image.open(img_file)

        # Extract text from the image using Tesseract OCR
        text = pytesseract.image_to_string(image)

        # Print the extracted text
        print(text)