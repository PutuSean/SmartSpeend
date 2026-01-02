def run_end_to_end(image_paths: list):
    # placeholder for end-to-end pipeline orchestration
    results = []
    from .ocr_pipeline import process_image_to_structured
    for p in image_paths:
        results.append(process_image_to_structured(p))
    return results
