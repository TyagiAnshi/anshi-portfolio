from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas


OUT = "Anshi_Tyagi_Resume_Cover_Page.pdf"
W, H = letter

NAVY = colors.HexColor("#17324D")
TEAL = colors.HexColor("#1A8C88")
GOLD = colors.HexColor("#D9A441")
INK = colors.HexColor("#243241")
MUTED = colors.HexColor("#5B6876")
LINE = colors.HexColor("#DDE5EA")
SOFT = colors.HexColor("#F3F7F8")


def para(c, text, x, y, width, style):
    p = Paragraph(text, style)
    _, h = p.wrap(width, H)
    p.drawOn(c, x, y - h)
    return y - h


def label(c, text, x, y, color=TEAL):
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(x, y, text.upper())
    return y - 0.18 * inch


def chip(c, text, x, y, pad_x=8, pad_y=4):
    c.setFont("Helvetica", 8.5)
    tw = stringWidth(text, "Helvetica", 8.5)
    w = tw + 2 * pad_x
    h = 18
    c.setFillColor(colors.white)
    c.setStrokeColor(colors.HexColor("#CFE1E3"))
    c.roundRect(x, y - h, w, h, 6, fill=1, stroke=1)
    c.setFillColor(INK)
    c.drawString(x + pad_x, y - h + pad_y + 1, text)
    return x + w + 6


def draw_metric(c, value, caption, x, y, w):
    c.setFillColor(colors.white)
    c.setStrokeColor(colors.HexColor("#CFE1E3"))
    c.roundRect(x, y - 0.82 * inch, w, 0.82 * inch, 8, fill=1, stroke=1)
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(x + w / 2, y - 0.31 * inch, value)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8.3)
    c.drawCentredString(x + w / 2, y - 0.55 * inch, caption)


def main():
    c = canvas.Canvas(OUT, pagesize=letter)
    c.setTitle("Anshi Tyagi Resume Cover Page")
    c.setAuthor("Anshi Tyagi")

    c.setFillColor(colors.white)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Header band
    c.setFillColor(NAVY)
    c.rect(0, H - 1.72 * inch, W, 1.72 * inch, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.rect(0, H - 1.72 * inch, W, 0.11 * inch, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.rect(0, H - 0.11 * inch, W, 0.11 * inch, fill=1, stroke=0)

    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 31)
    c.drawString(0.72 * inch, H - 0.73 * inch, "ANSHI TYAGI")
    c.setFont("Helvetica", 13.2)
    c.drawString(
        0.73 * inch,
        H - 1.08 * inch,
        "Computer Science Undergraduate | Artificial Intelligence & Machine Learning",
    )
    c.setFont("Helvetica", 9.4)
    c.drawString(
        0.73 * inch,
        H - 1.39 * inch,
        "+91 9761709080  |  tyagianshi2005@gmail.com  |  linkedin.com/in/anshityagi  |  github.com/TyagiAnshi",
    )

    left = 0.72 * inch
    right = W - 0.72 * inch
    y = H - 2.12 * inch

    lead_style = ParagraphStyle(
        "Lead",
        fontName="Helvetica",
        fontSize=10.8,
        leading=16,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=0,
    )
    small_style = ParagraphStyle(
        "Small",
        fontName="Helvetica",
        fontSize=9.2,
        leading=13,
        textColor=INK,
        alignment=TA_LEFT,
    )
    bullet_style = ParagraphStyle(
        "Bullet",
        fontName="Helvetica",
        fontSize=9.1,
        leading=12.6,
        leftIndent=11,
        firstLineIndent=-8,
        textColor=INK,
    )
    center_style = ParagraphStyle(
        "Center",
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        textColor=MUTED,
    )

    y = label(c, "Profile", left, y)
    y = para(
        c,
        "AI/ML-focused computer science undergraduate with hands-on experience across anomaly detection, regression modeling, classification, data analysis, model evaluation, Flask REST APIs, and Streamlit dashboards. Brings a practical project portfolio with measurable outcomes and a clear habit of technical documentation and reliable delivery.",
        left,
        y,
        right - left,
        lead_style,
    )

    y -= 0.28 * inch
    metric_w = (right - left - 0.24 * inch) / 3
    draw_metric(c, "0.9583", "ROC-AUC in turnover prediction", left, y, metric_w)
    draw_metric(c, "88.15%", "Classification accuracy achieved", left + metric_w + 0.12 * inch, y, metric_w)
    draw_metric(c, "0.87", "R-squared salary model score", left + 2 * (metric_w + 0.12 * inch), y, metric_w)

    y -= 1.18 * inch
    col_gap = 0.34 * inch
    col_w = (right - left - col_gap) / 2

    y_left = label(c, "Project Highlights", left, y)
    projects = [
        ("Credit Card Fraud Detection System", "Built an anomaly detection and classification pipeline on 284,000+ transaction records using Isolation Forest, LOF, XGBoost, SMOTE, and Streamlit visual scoring."),
        ("Smart Salary Predictor", "Created a full-stack ML app with Flask REST API and Streamlit front end, benchmarking 5+ regression algorithms and surfacing real-time analytics."),
        ("Employee Turnover Prediction System", "Delivered preprocessing, feature engineering, cross-validation, model comparison, API endpoints, dashboard workflows, and feature-importance views."),
    ]
    for title, body in projects:
        y_left = para(c, f"<b>{title}</b><br/>{body}", left, y_left, col_w, small_style)
        y_left -= 0.13 * inch

    x2 = left + col_w + col_gap
    y_right = label(c, "Core Strengths", x2, y)
    bullets = [
        "Machine learning workflows: preprocessing, feature engineering, model training, evaluation, and interpretation.",
        "Python ecosystem: scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Plotly, Flask, Streamlit, MySQL.",
        "Computer science foundation: DSA, OOP, DBMS, operating systems, software engineering, and networks.",
        "Professional habits: collaboration, stakeholder communication, technical documentation, ownership, and adaptability.",
    ]
    for item in bullets:
        y_right = para(c, f"• {item}", x2, y_right, col_w, bullet_style)
        y_right -= 0.05 * inch

    y = min(y_left, y_right) - 0.2 * inch
    c.setStrokeColor(LINE)
    c.line(left, y, right, y)
    y -= 0.32 * inch

    y = label(c, "Education & Current Role", left, y)
    c.setFillColor(SOFT)
    c.setStrokeColor(colors.HexColor("#DCE8EA"))
    c.roundRect(left, y - 0.92 * inch, right - left, 0.92 * inch, 8, fill=1, stroke=1)
    y_card = y - 0.2 * inch
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 10.2)
    c.drawString(left + 0.18 * inch, y_card, "Machine Learning Intern - Elevate Labs")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8.8)
    c.drawRightString(right - 0.18 * inch, y_card, "Apr 2025 - Present")
    c.setFillColor(INK)
    c.setFont("Helvetica", 9.4)
    c.drawString(left + 0.18 * inch, y_card - 0.28 * inch, "B.Tech in Computer Science and Engineering, AIML")
    c.setFillColor(MUTED)
    c.drawString(left + 0.18 * inch, y_card - 0.48 * inch, "JSS Academy of Technical Education, Noida")
    c.setFillColor(MUTED)
    c.drawRightString(right - 0.18 * inch, y_card - 0.28 * inch, "Oct 2023 - Present | 7.9")
    y -= 1.22 * inch

    y = label(c, "Technical Toolbox", left, y)
    chips = [
        "Python",
        "C++",
        "SQL",
        "scikit-learn",
        "Pandas",
        "NumPy",
        "Flask",
        "Streamlit",
        "GitHub",
        "Model Evaluation",
        "Feature Engineering",
        "Cross-Validation",
    ]
    x = left
    for item in chips:
        c.setFont("Helvetica", 8.5)
        width = stringWidth(item, "Helvetica", 8.5) + 16
        if x + width > right:
            x = left
            y -= 0.28 * inch
        x = chip(c, item, x, y)

    c.setStrokeColor(LINE)
    c.line(left, 0.62 * inch, right, 0.62 * inch)
    para(
        c,
        "Resume cover page prepared for applications in machine learning, data science, AI engineering, and software roles.",
        left,
        0.47 * inch,
        right - left,
        center_style,
    )

    c.showPage()
    c.save()


if __name__ == "__main__":
    main()
