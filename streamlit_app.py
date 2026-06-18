from pathlib import Path

import requests
import streamlit as st

from portfolio_data import PORTFOLIO


API_URL = "http://127.0.0.1:5000/api/portfolio"
BASE_DIR = Path(__file__).resolve().parent


st.set_page_config(
    page_title="Anshi Tyagi | AI/ML Portfolio",
    page_icon="AT",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def load_portfolio():
    try:
        response = requests.get(API_URL, timeout=1.5)
        response.raise_for_status()
        return response.json(), True
    except requests.RequestException:
        return PORTFOLIO, False


def read_file(name):
    path = BASE_DIR / name
    return path.read_bytes() if path.exists() else None


portfolio, api_connected = load_portfolio()
contact = portfolio["contact"]

st.markdown(
    """
    <style>
      :root {
        --black: #111111;
        --ink: #1f1f24;
        --muted: #5f6068;
        --pink: #ff5f9e;
        --pink-soft: #ffe3ef;
        --pink-mid: #ff9ac2;
        --gray: #f2f2f4;
        --gray-2: #e1e1e6;
        --white: #ffffff;
        --line: rgba(17, 17, 17, 0.14);
      }
      .stApp {
        background:
          radial-gradient(circle at 10% 0%, rgba(255,95,158,.18), transparent 28rem),
          linear-gradient(135deg, #ffffff 0%, var(--gray) 54%, var(--pink-soft) 100%);
        color: var(--black);
      }
      [data-testid="stHeader"] {
        background: rgba(255,255,255,.84);
        backdrop-filter: blur(14px);
      }
      .stApp, .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span, label {
        color: var(--black);
      }
      .block-container {
        max-width: 1180px;
        padding-top: 3.25rem;
        padding-bottom: 4rem;
      }
      .eyebrow {
        color: var(--pink);
        font-size: .78rem;
        font-weight: 900;
        letter-spacing: 0;
        text-transform: uppercase;
        margin: 0 0 .5rem;
      }
      .hero-title {
        color: var(--black);
        font-size: clamp(3.4rem, 8vw, 7rem);
        font-weight: 900;
        line-height: .9;
        letter-spacing: 0;
        margin: 0;
      }
      .hero-role {
        color: var(--pink);
        font-size: clamp(1.25rem, 2.2vw, 1.8rem);
        font-weight: 850;
        line-height: 1.16;
        margin: .9rem 0 1rem;
      }
      .hero-copy {
        color: var(--ink);
        font-size: 1.08rem;
        line-height: 1.65;
        max-width: 46rem;
      }
      .status-pill {
        display: inline-flex;
        align-items: center;
        gap: .45rem;
        border: 1px solid var(--line);
        border-radius: 999px;
        padding: .42rem .78rem;
        background: rgba(255,255,255,.84);
        color: var(--black);
        font-size: .82rem;
        font-weight: 800;
      }
      .metric-card, .project-card, .panel-card, .timeline-card {
        border: 1px solid var(--line);
        border-radius: 8px;
        background: rgba(255,255,255,.9);
        box-shadow: 0 18px 44px rgba(17,17,17,.08);
      }
      .metric-card {
        min-height: 9.2rem;
        padding: 1.35rem;
      }
      .metric-card strong {
        display: block;
        color: var(--black);
        font-size: 2.45rem;
        line-height: 1;
      }
      .metric-card span {
        display: block;
        color: var(--pink);
        font-weight: 900;
        margin: .25rem 0 .6rem;
      }
      .metric-card p, .project-card p, .panel-card p, .timeline-card p {
        color: var(--muted);
      }
      .project-card, .panel-card, .timeline-card {
        padding: 1.35rem;
        height: 100%;
      }
      .project-type {
        color: var(--pink);
        font-size: .76rem;
        font-weight: 900;
        text-transform: uppercase;
        margin-bottom: .45rem;
      }
      .chip {
        display: inline-block;
        border: 1px solid rgba(17,17,17,.16);
        border-radius: 999px;
        padding: .35rem .58rem;
        margin: .18rem .18rem .18rem 0;
        background: var(--pink-soft);
        color: var(--black);
        font-size: .78rem;
        font-weight: 800;
      }
      .section-title {
        color: var(--black);
        font-size: clamp(1.9rem, 4vw, 3.2rem);
        font-weight: 900;
        line-height: 1.04;
        margin: 0 0 1.4rem;
      }
      .divider {
        height: 1px;
        margin: 2.5rem 0;
        background: var(--line);
      }
      .cover-image img {
        border: 1px solid var(--line);
        border-radius: 8px;
        box-shadow: 0 24px 70px rgba(17,17,17,.16);
      }
      .ai-band {
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 1.25rem;
        background: linear-gradient(135deg, #ffffff, var(--pink-soft));
        height: 100%;
      }
      .prompt-box {
        border-left: 5px solid var(--pink);
        border-radius: 8px;
        padding: 1rem 1.1rem;
        background: #ffffff;
        color: var(--black);
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
        line-height: 1.55;
      }
      div.stButton > button, div.stDownloadButton > button, div[data-testid="stLinkButton"] > a {
        border: 1px solid var(--black);
        border-radius: 8px;
        background: var(--black);
        color: #ffffff;
        font-weight: 900;
      }
      div.stButton > button:hover, div.stDownloadButton > button:hover, div[data-testid="stLinkButton"] > a:hover {
        border-color: var(--pink);
        background: var(--pink);
        color: var(--black);
      }
    </style>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([1.45, 0.85], gap="large")
with left:
    st.markdown('<p class="eyebrow">AI/ML Portfolio App</p>', unsafe_allow_html=True)
    st.markdown(f'<h1 class="hero-title">{portfolio["name"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="hero-role">{portfolio["role"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="hero-copy">{portfolio["summary"]}</p>', unsafe_allow_html=True)
    st.markdown(
        f'<span class="status-pill">{"Flask API connected" if api_connected else "Using local data fallback"}</span>',
        unsafe_allow_html=True,
    )

    doc_cols = st.columns(2)
    resume_bytes = read_file(portfolio["documents"]["resume"])
    cover_bytes = read_file(portfolio["documents"]["cover_page"])
    with doc_cols[0]:
        st.download_button(
            "Download Resume",
            data=resume_bytes or b"",
            file_name=portfolio["documents"]["resume"],
            mime="application/pdf",
            disabled=resume_bytes is None,
            use_container_width=True,
        )
    with doc_cols[1]:
        st.download_button(
            "Download Cover Page",
            data=cover_bytes or b"",
            file_name=portfolio["documents"]["cover_page"],
            mime="application/pdf",
            disabled=cover_bytes is None,
            use_container_width=True,
        )

with right:
    preview = BASE_DIR / "cover_preview.png"
    if preview.exists():
        st.markdown('<div class="cover-image">', unsafe_allow_html=True)
        st.image(str(preview), use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

metric_cols = st.columns(4)
for column, metric in zip(metric_cols, portfolio["metrics"]):
    with column:
        st.markdown(
            f"""
            <div class="metric-card">
              <strong>{metric["value"]}</strong>
              <span>{metric["label"]}</span>
              <p>{metric["detail"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<p class="eyebrow">AI Direction</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Prompt engineering and AI integration focus</h2>', unsafe_allow_html=True)

focus_cols = st.columns(3)
for column, item in zip(focus_cols, portfolio["focus_areas"]):
    with column:
        st.markdown(
            f"""
            <div class="ai-band">
              <h3>{item["title"]}</h3>
              <p>{item["description"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<p class="eyebrow">Featured Projects</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Selected AI and machine learning work</h2>', unsafe_allow_html=True)

project_cols = st.columns(3)
for column, project in zip(project_cols, portfolio["projects"]):
    with column:
        chips = "".join(f'<span class="chip">{item}</span>' for item in project["stack"])
        highlights = "".join(f"<li>{item}</li>" for item in project["highlights"])
        st.markdown(
            f"""
            <div class="project-card">
              <p class="project-type">{project["type"]}</p>
              <h3>{project["title"]}</h3>
              <p>{project["description"]}</p>
              <ul>{highlights}</ul>
              <div>{chips}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<p class="eyebrow">Technical Skill Map</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">What I can build with</h2>', unsafe_allow_html=True)

skill_cols = st.columns(3)
for index, (group, skills) in enumerate(portfolio["skills"].items()):
    with skill_cols[index % 3]:
        chips = "".join(f'<span class="chip">{skill}</span>' for skill in skills)
        st.markdown(
            f"""
            <div class="panel-card">
              <h3>{group}</h3>
              <div>{chips}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<p class="eyebrow">Interactive Prompt Lab</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Generate a polished AI workflow prompt</h2>', unsafe_allow_html=True)
prompt_topic = st.selectbox("Choose a prompt use case", list(portfolio["prompt_examples"].keys()))
st.markdown(
    f"""
    <div class="prompt-box">
      {portfolio["prompt_examples"][prompt_topic]}
    </div>
    """,
    unsafe_allow_html=True,
)
st.caption("This section shows how I think about prompt structure: role, task, context, output format, and evaluation criteria.")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
exp_col, edu_col = st.columns([1, 1], gap="large")

with exp_col:
    st.markdown('<p class="eyebrow">Experience</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Current role</h2>', unsafe_allow_html=True)
    for item in portfolio["experience"]:
        details = "".join(f"<li>{detail}</li>" for detail in item["details"])
        st.markdown(
            f"""
            <div class="timeline-card">
              <p class="project-type">{item["period"]}</p>
              <h3>{item["title"]} - {item["organization"]}</h3>
              <ul>{details}</ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

with edu_col:
    st.markdown('<p class="eyebrow">Education</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Academic path</h2>', unsafe_allow_html=True)
    for item in portfolio["education"]:
        st.markdown(
            f"""
            <div class="timeline-card">
              <p class="project-type">{item["period"]}</p>
              <h3>{item["degree"]}</h3>
              <p>{item["school"]} | {item["score"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<p class="eyebrow">Achievements</p>', unsafe_allow_html=True)
for achievement in portfolio["achievements"]:
    st.success(achievement)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<p class="eyebrow">Contact</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Open to AI/ML, data science, and software opportunities.</h2>', unsafe_allow_html=True)
contact_cols = st.columns(4)
contact_cols[0].link_button("Email", f"mailto:{contact['email']}", use_container_width=True)
contact_cols[1].link_button("Call", f"tel:{contact['phone'].replace(' ', '')}", use_container_width=True)
contact_cols[2].link_button("LinkedIn", contact["linkedin"], use_container_width=True)
contact_cols[3].link_button("GitHub", contact["github"], use_container_width=True)
