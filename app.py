import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from huggingface_hub import InferenceClient
import os

from resume_parser import extract_text
from skills import data_science_skills
from career_roles import recommend_role
from job_recommender import recommend_jobs
from dotenv import load_dotenv

# ----------------------------
# HUGGING FACE CLIENT
# ----------------------------
client = InferenceClient(
    token=os.getenv("HF_TOKEN")
)


# ----------------------------
# AI FEEDBACK FUNCTION
# ----------------------------
def get_ai_feedback(resume_text):

    prompt = f"""
Analyze the following resume and provide:

1. Strengths
2. Weaknesses
3. Missing skills
4. Suggestions to improve the resume for Data Science roles.

Resume:
{resume_text[:2000]}
"""

    try:
        response = client.chat_completion(
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=400
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ AI Error: {str(e)}"


# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="AI Career Navigator", layout="wide")


# ----------------------------
# UI STYLE
# ----------------------------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

.big-title{
font-size:55px;
font-weight:700;
}

.subtitle{
font-size:20px;
opacity:0.8;
}

.card{
background: rgba(255,255,255,0.08);
padding:20px;
border-radius:15px;
backdrop-filter: blur(10px);
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)


# ----------------------------
# HERO SECTION
# ----------------------------
col1,col2 = st.columns([3,1])

with col1:
    st.markdown('<p class="big-title">🤖 AI Career Navigator</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Smart Resume Analyzer & Career Recommendation Platform</p>', unsafe_allow_html=True)

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=120)

st.divider()


# ----------------------------
# FILE UPLOAD
# ----------------------------
file = st.file_uploader("Upload Resume (PDF)", type="pdf")


if file:

    text = extract_text(file)

    found_skills = []
    missing_skills = []

    for skill in data_science_skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    score = int((len(found_skills) / len(data_science_skills)) * 100)

    role = recommend_role(found_skills)

    jobs = recommend_jobs(found_skills)

    tab1,tab2,tab3,tab4 = st.tabs([
        "📄 Resume Analysis",
        "📊 Skill Dashboard",
        "🤖 AI Feedback",
        "💼 Job Recommendations"
    ])


# ----------------------------
# TAB 1
# ----------------------------
    with tab1:

        col1,col2,col3 = st.columns(3)

        col1.metric("Skills Found", len(found_skills))
        col2.metric("Missing Skills", len(missing_skills))
        col3.metric("Career Role", role)

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': "ATS Resume Score"},
            gauge={
                'axis': {'range':[0,100]},
                'bar': {'color': "#00FFD1"},
                'steps':[
                    {'range':[0,50],'color':'#ff4b4b'},
                    {'range':[50,80],'color':'#f9c74f'},
                    {'range':[80,100],'color':'#43aa8b'}
                ]
            }
        ))

        st.plotly_chart(fig, use_container_width=True)


# ----------------------------
# TAB 2
# ----------------------------
    with tab2:

        st.subheader("Detected Skills")
        st.write(found_skills)

        st.subheader("Missing Skills")
        st.write(missing_skills)

        chart_data = {
            "Category":["Detected Skills","Missing Skills"],
            "Count":[len(found_skills),len(missing_skills)]
        }

        fig = px.pie(chart_data, names="Category", values="Count")

        st.plotly_chart(fig,use_container_width=True)


# ----------------------------
# TAB 3
# ----------------------------
    with tab3:

        st.subheader("🤖 AI Resume Feedback")

        if st.button("Generate AI Feedback"):

            with st.spinner("AI is analyzing your resume..."):

                feedback = get_ai_feedback(text)

            st.success("AI Analysis Complete")

            st.write(feedback)


# ----------------------------
# TAB 4
# ----------------------------
    with tab4:

        st.subheader("Recommended Jobs")

        for job in jobs:

            st.markdown(f"""
            <div class="card">
            💼 <b>{job}</b>
            <br>
            Recommended based on detected skills
            </div>
            """, unsafe_allow_html=True)