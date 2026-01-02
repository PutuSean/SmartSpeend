from src.ocr.parser import parse_receipt_text

def test_parse_simple_text():
    text = """MINIMARKET
    2021-05-01
    Item A 10.000
    Total: 10.000
    """
    parsed = parse_receipt_text(text)
    assert 'amount' in parsed
    assert parsed['merchant'] == 'MINIMARKET'
