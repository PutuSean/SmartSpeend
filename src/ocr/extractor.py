# Example OCR wrapper (pytesseract). Replace with PaddleOCR if available.
import pytesseract
from PIL import Image

def ocr_image(img_path: str) -> str:
    text = pytesseract.image_to_string(Image.open(img_path), lang='ind')
    return text
