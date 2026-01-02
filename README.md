# Smart Spend OCR — Starter Repository

Starter repository for the Smart Spend OCR Edition project (OCR → ML → Dashboard).
This scaffold includes production-ready structure, example modules, and basic templates so you can push directly to GitHub and start collaborating.

## What is included
- `data/` folders (placeholders)
- `notebooks/` starter notebooks (empty placeholders)
- `src/` modular code (OCR, data, features, models, pipeline, dashboard)
- `models/` placeholder for saved models
- `tests/` basic unit test templates
- `docker/` Dockerfile and docker-compose.yml
- `docs/` basic PRD and dataset rules placeholders
- `requirements.txt` minimal deps

## How to use
1. Extract the repository and `cd` into the folder.
2. Create a Python virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run tests:
   ```bash
   pytest -q
   ```
4. Start Streamlit dashboard (when implemented):
   ```bash
   streamlit run src/dashboard/app.py
   ```

## Next steps (suggested)
- Replace synthetic placeholders in `data/raw/` with actual dataset files.
- Implement OCR engine in `src/ocr/` (recommendation: PaddleOCR or EasyOCR).
- Train models and save to `models/`.
- Configure CI/CD on GitHub Actions for tests & linting.

