import streamlit as st
import google.generativeai as genai

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Learning Companion",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Learning Companion")

# -----------------------------
# GEMINI CONFIG
# -----------------------------
API_KEY = st.sidebar.text_input(
    "AQ.Ab8RN6Jn7AHuF-WiYKDXbdJD5EwbAa8xRF8dZHXJs942xC-2cg",
    type="password"
)

if API_KEY:
    genai.configure(api_key=API_KEY)
    gemini_model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

# -----------------------------
# LOAD MODELS
# -----------------------------
with st.spinner("Loading AI Models..."):

    reader = easyocr.Reader(['en'])

    sbert = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

# -----------------------------
# OCR FUNCTION
# -----------------------------
def extract_text(uploaded_file):

    temp_path = "temp.jpg"

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    result = reader.readtext(temp_path)

    text = " ".join(
        [item[1] for item in result]
    )

    return text

# -----------------------------
# FILE UPLOADS
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    teacher_file = st.file_uploader(
        "📘 Upload Teacher Answer Sheet",
        type=["jpg", "jpeg", "png"]
    )

with col2:

    student_file = st.file_uploader(
        "📝 Upload Student Answer Sheet",
        type=["jpg", "jpeg", "png"]
    )

# -----------------------------
# PROCESS
# -----------------------------
if teacher_file and student_file:

    with st.spinner("Extracting Text..."):

        teacher_answer = extract_text(
            teacher_file
        )

        student_answer = extract_text(
            student_file
        )

    # -------------------------
    # DISPLAY OCR TEXT
    # -------------------------
    st.subheader("📘 Teacher Answer")

    st.write(teacher_answer)

    st.subheader("📝 Student Answer")

    st.write(student_answer)

    # -------------------------
    # SBERT SIMILARITY
    # -------------------------
    emb1 = sbert.encode(
        teacher_answer,
        convert_to_tensor=True
    )

    emb2 = sbert.encode(
        student_answer,
        convert_to_tensor=True
    )

    similarity = float(
        util.cos_sim(
            emb1,
            emb2
        )
    )

    marks = round(
        similarity * 10,
        2
    )

    # -------------------------
    # GEMINI FEEDBACK
    # -------------------------
    feedback = "Gemini feedback unavailable."

    if API_KEY:

        try:

            prompt = f"""
            You are an academic evaluator.

            Teacher Answer:
            {teacher_answer}

            Student Answer:
            {student_answer}

            Similarity Score:
            {similarity:.3f}

            Marks:
            {marks}/10

            Evaluate the student answer.

            Give:

            1. Strengths

            2. Missing Concepts

            3. Suggestions for Improvement

            4. Final Summary
            """

            response = gemini_model.generate_content(
                prompt
            )

            feedback = response.text

        except Exception as e:

            feedback = f"""
Gemini Error:

{str(e)}

Check your API key.
"""

    # -------------------------
    # RESULTS
    # -------------------------
    st.subheader("📊 Evaluation Results")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Similarity Score",
            round(similarity, 3)
        )

    with c2:

        st.metric(
            "Marks",
            f"{marks}/10"
        )

    st.progress(
        min(
            max(similarity, 0),
            1
        )
    )

    st.subheader("🤖 AI Feedback")

    st.write(feedback)
