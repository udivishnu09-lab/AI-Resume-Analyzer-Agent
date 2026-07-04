# analyzer.py

from skills import TECHNICAL_SKILLS, SOFT_SKILLS, JOB_ROLES


def analyze_resume(resume_text, job_role=""):

    text = resume_text.lower()

    # -----------------------------
    # Skill Extraction
    # -----------------------------
    technical = []

    for skill in TECHNICAL_SKILLS:
        if skill.lower() in text:
            technical.append(skill.title())

    soft = []

    for skill in SOFT_SKILLS:
        if skill.lower() in text:
            soft.append(skill.title())

    # -----------------------------
    # ATS Score
    # -----------------------------
    ats = 40

    ats += min(len(technical) * 3, 30)

    if "project" in text:
        ats += 10

    if "internship" in text:
        ats += 10

    if "certificate" in text or "certification" in text:
        ats += 5

    if "github" in text:
        ats += 5

    ats = min(ats, 100)

    # -----------------------------
    # Strengths
    # -----------------------------
    strengths = []

    if len(technical) >= 8:
        strengths.append("Strong technical skill set.")

    if "project" in text:
        strengths.append("Includes project experience.")

    if "internship" in text:
        strengths.append("Has internship experience.")

    if "github" in text:
        strengths.append("GitHub profile mentioned.")

    if "machine learning" in text:
        strengths.append("Machine Learning knowledge detected.")

    # -----------------------------
    # Weaknesses
    # -----------------------------
    weaknesses = []

    if "internship" not in text:
        weaknesses.append("Internship experience missing.")

    if "certificate" not in text and "certification" not in text:
        weaknesses.append("Certifications missing.")

    if "github" not in text:
        weaknesses.append("GitHub profile not included.")

    if len(technical) < 8:
        weaknesses.append("Add more technical skills.")

    # -----------------------------
    # Recommendations
    # -----------------------------
    recommendations = []

    if "docker" not in text:
        recommendations.append("Learn Docker.")

    if "aws" not in text:
        recommendations.append("Learn AWS Cloud.")

    if "kubernetes" not in text:
        recommendations.append("Learn Kubernetes.")

    if "communication" not in text:
        recommendations.append("Mention communication skills.")

    if "linkedin" not in text:
        recommendations.append("Include LinkedIn profile.")

    # -----------------------------
    # Job Match
    # -----------------------------
    match_percent = 0
    matched = []
    missing = []

    if job_role in JOB_ROLES:

        required = JOB_ROLES[job_role]

        for skill in required:

            if skill.lower() in text:
                matched.append(skill.title())
            else:
                missing.append(skill.title())

        match_percent = int((len(matched) / len(required)) * 100)

    # -----------------------------
    # Recommended Roles
    # -----------------------------
    recommended_roles = []

    for role, skills in JOB_ROLES.items():

        count = 0

        for skill in skills:

            if skill.lower() in text:
                count += 1

        if count >= 3:
            recommended_roles.append(role)

    if not recommended_roles:
        recommended_roles.append("Software Developer")

    # -----------------------------
    # Interview Questions
    # -----------------------------
    questions = [

        "Tell me about yourself.",

        "Explain your final year project.",

        "What are your strengths?",

        "What is Object-Oriented Programming?",

        "Explain SQL JOIN.",

        "Difference between List and Tuple in Python?",

        "Explain Git and GitHub.",

        "What is Machine Learning?",

        "Why should we hire you?",

        "Where do you see yourself in 5 years?"
    ]

    return {

        "technical_skills": technical,

        "soft_skills": soft,

        "ats_score": ats,

        "strengths": strengths,

        "weaknesses": weaknesses,

        "recommendations": recommendations,

        "job_match": match_percent,

        "matched_skills": matched,

        "missing_skills": missing,

        "recommended_roles": recommended_roles,

        "interview_questions": questions
    }