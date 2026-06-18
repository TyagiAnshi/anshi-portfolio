from pathlib import Path

from flask import Flask, jsonify, send_from_directory

from portfolio_data import PORTFOLIO


BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(
        {
            "message": "Anshi Tyagi portfolio API",
            "endpoints": ["/api/portfolio", "/documents/resume", "/documents/cover-page"],
        }
    )


@app.get("/api/portfolio")
def portfolio():
    return jsonify(PORTFOLIO)


@app.get("/documents/resume")
def resume():
    return send_from_directory(BASE_DIR, PORTFOLIO["documents"]["resume"], as_attachment=False)


@app.get("/documents/cover-page")
def cover_page():
    return send_from_directory(BASE_DIR, PORTFOLIO["documents"]["cover_page"], as_attachment=False)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
