from ..ocr.extractor import ocr_image
from ..ocr.parser import parse_receipt_text

def process_image_to_structured(img_path: str):
    text = ocr_image(img_path)
    parsed = parse_receipt_text(text)
    return parsed
