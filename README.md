# Anshi Tyagi Portfolio

This repository contains two portfolio versions:

- `index.html` and `styles.css`: a static GitHub Pages portfolio.
- `flask_app.py` and `streamlit_app.py`: an interactive Flask + Streamlit portfolio app.

## Run The Flask + Streamlit Portfolio

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Start the Flask API in one terminal:

```bash
python flask_app.py
```

Start the Streamlit app in another terminal:

```bash
streamlit run streamlit_app.py
```

Open the Streamlit URL shown in the terminal, usually:

```text
http://localhost:8501
```

The Streamlit app reads portfolio data from the Flask API at `http://127.0.0.1:5000/api/portfolio`. If Flask is not running, Streamlit falls back to the local data in `portfolio_data.py`.
