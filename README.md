🤖 AI Resume Analyzer & Career Navigator

An AI-powered Resume Analyzer built with Python that extracts skills from resumes, calculates an ATS score, provides AI-based feedback, and recommends suitable career roles and jobs for Data Science aspirants.

This project helps candidates understand their resume strength, identify missing skills, and improve their chances of getting shortlisted.

🚀 Features:-
1. 📄 Resume Parsing
Extracts text from uploaded PDF resumes.

2. 🧠 Skill Detection
Identifies relevant Data Science skills from the resume.

3. 📊 ATS Resume Score
Calculates a score based on detected skills.

4. 🎯 Career Role Recommendation
Suggests suitable roles such as:
    A. Data Scientist
    B. Data Analyst
    C. Machine Learning Engineer

5. 💼 Job Recommendations
Suggests potential job positions based on detected skills.

6. 🤖 AI Resume Feedback
Uses AI models to provide:
      Strengths
      Weaknesses
      Missing skills
      Resume improvement suggestions

7. 📊 Interactive Dashboard
Built with Streamlit and Plotly for visualization.

🛠 Technologies Used
      Python
      Streamlit
      Plotly
      Hugging Face Inference API
      Natural Language Processing (NLP)
      PDF Parsing

Libraries:
      streamlit
      plotly
      huggingface_hub
      pdfplumber
      python-dotenv


📂 Project Structure
resume-analyzer
      │
      ├── app.py
      ├── resume_parser.py
      ├── skills.py
      ├── career_roles.py
      ├── job_recommender.py
      ├── utils.py
      ├── requirements.txt
      ├── style.css
      └── .gitignore


⚙️ Installation
1. Clone the repository:
    git clone https://github.com/yourusername/resume-analyzer.git

2. Move to the project folder:
    cd resume-analyzer

4. Install dependencies:
    pip install -r requirements.txt

🔑 Environment Variables
Create a .env file in the project root and add your Hugging Face API token:
HF_TOKEN=your_huggingface_token

▶️ Run the Application
    Start the Streamlit app:
    streamlit run app.py
    The application will open in your browser.

📊 Example Output
    The system provides:
    ATS Resume Score
    Detected Skills
    Missing Skills
    AI Resume Feedback
    Career Role Recommendation
    Job Suggestions

🎯 Future Improvements
  Resume vs Job Description Matching
  AI Cover Letter Generator
  Real-time Job Listings Integration
  Skill Gap Learning Roadmap

👨‍💻 Author
Tirth Patel
B.Tech – Artificial Intelligence & Data Science
Aspiring Data Scientist

LinkedIn: https://www.linkedin.com/in/tirth-patel-9a939a287/
