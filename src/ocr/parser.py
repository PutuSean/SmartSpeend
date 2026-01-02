import re
from typing import Dict, Any

def parse_receipt_text(text: str) -> Dict[str, Any]:
    # Very simple examples: adjust regex for production use
    data = {}
    date_match = re.search(r'(\d{2}/\d{2}/\d{4})|(\d{4}-\d{2}-\d{2})', text)
    if date_match:
        data['date'] = date_match.group(0)
    amt_match = re.search(r'Total\s*[:\-]?\s*(\d+[\.,]?\d+)', text, re.I)
    if amt_match:
        data['amount'] = amt_match.group(1)
    # merchant heuristics
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    data['merchant'] = lines[0] if lines else None
    data['raw_text'] = text
    return data
