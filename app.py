import streamlit as st
from pdf_parser import extract_text_from_pdf
from analyzer import analyze_resume

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer Agent",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main{
    background-color:#f5f7fb;
}

.title{
    text-align:center;
    color:#1f4e79;
    font-size:40px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
}

.box{
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

h2{
    color:#1f4e79;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    "<div class='title'>📄 AI Resume Analyzer Agent</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Offline ATS Resume Analyzer (No API Required)</div>",
    unsafe_allow_html=True
)

st.write("")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Resume Analyzer")

job_role = st.sidebar.selectbox(
    "Select Target Job Role",
    [
        "Python Developer",
        "Data Analyst",
        "Machine Learning Engineer",
        "Frontend Developer",
        "Full Stack Developer",
        "Data Scientist"
    ]
)

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file is None:
    st.info("Please upload your resume PDF.")
    st.stop()

# -----------------------------
# Read Resume
# -----------------------------
resume_text = extract_text_from_pdf(uploaded_file)

if resume_text.startswith("ERROR"):
    st.error(resume_text)
    st.stop()

st.success("Resume uploaded successfully.")

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("Analyze Resume"):

    with st.spinner("Analyzing Resume..."):

        results = analyze_resume(
            resume_text,
            job_role
        )

        st.success("Analysis Completed Successfully!")

        st.write("")

        # ATS Score
        st.markdown("## 🎯 ATS Score")

        st.progress(results["ats_score"] / 100)

        st.metric(
            "ATS Score",
            f'{results["ats_score"]}/100'
        )

        st.write("---")

                # -----------------------------
        # Technical Skills
        # -----------------------------
        st.markdown("## 💻 Technical Skills")

        if results["technical_skills"]:

            for skill in results["technical_skills"]:
                st.success(f"✅ {skill}")

        else:
            st.warning("No technical skills detected.")

        st.write("---")

        # -----------------------------
        # Soft Skills
        # -----------------------------
        st.markdown("## 🤝 Soft Skills")

        if results["soft_skills"]:

            for skill in results["soft_skills"]:
                st.info(f"✔ {skill}")

        else:
            st.warning("No soft skills detected.")

        st.write("---")

        # -----------------------------
        # Job Match
        # -----------------------------
        st.markdown("## 💼 Job Match")

        st.metric(
            "Match Percentage",
            f'{results["job_match"]}%'
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Matched Skills")

            if results["matched_skills"]:

                for skill in results["matched_skills"]:
                    st.success(skill)

            else:
                st.write("No matching skills.")

        with col2:

            st.subheader("Missing Skills")

            if results["missing_skills"]:

                for skill in results["missing_skills"]:
                    st.error(skill)

            else:
                st.write("No missing skills.")

        st.write("---")

        # -----------------------------
        # Strengths
        # -----------------------------
        st.markdown("## 💪 Strengths")

        if results["strengths"]:

            for strength in results["strengths"]:
                st.success(f"✔ {strength}")

        else:
            st.info("No strengths detected.")

        st.write("---")

        # -----------------------------
        # Weaknesses
        # -----------------------------
        st.markdown("## ⚠ Weaknesses")

        if results["weaknesses"]:

            for weakness in results["weaknesses"]:
                st.warning(f"• {weakness}")

        else:
            st.success("No weaknesses found.")

        st.write("---")

                # -----------------------------
        # Recommendations
        # -----------------------------
        st.markdown("## 💡 Recommendations")

        if results["recommendations"]:

            for recommendation in results["recommendations"]:
                st.info(f"👉 {recommendation}")

        else:
            st.success("Your resume looks good!")

        st.write("---")

        # -----------------------------
        # Recommended Job Roles
        # -----------------------------
        st.markdown("## 💼 Recommended Job Roles")

        if results["recommended_roles"]:

            for role in results["recommended_roles"]:
                st.success(f"✅ {role}")

        else:
            st.write("No job roles recommended.")

        st.write("---")

        # -----------------------------
        # Interview Questions
        # -----------------------------
        st.markdown("## 🎤 Interview Questions")

        for i, question in enumerate(results["interview_questions"], start=1):
            st.write(f"**{i}.** {question}")

        st.write("---")

        # -----------------------------
        # Resume Summary
        # -----------------------------
        st.markdown("## 📋 Resume Summary")

        st.write(f"**Technical Skills Found:** {len(results['technical_skills'])}")
        st.write(f"**Soft Skills Found:** {len(results['soft_skills'])}")
        st.write(f"**ATS Score:** {results['ats_score']}/100")
        st.write(f"**Job Match:** {results['job_match']}%")

        if results["ats_score"] >= 85:
            st.success("Excellent Resume! Ready for most ATS systems.")
        elif results["ats_score"] >= 70:
            st.info("Good Resume. A few improvements can make it stronger.")
        else:
            st.warning("Resume needs improvement to increase ATS performance.")

        st.write("---")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <hr>
    <center>
        <h4>📄 AI Resume Analyzer Agent</h4>
        <p>Offline Version • No API Required</p>
        <p>Developed using Python & Streamlit</p>
    </center>
    """,
    unsafe_allow_html=True
)