def recommend_role(skills):

    if "Deep Learning" in skills:
        return "AI Engineer"

    if "Machine Learning" in skills:
        return "Machine Learning Engineer"

    if "SQL" in skills and "Python" in skills:
        return "Data Scientist"

    if "Power BI" in skills or "Tableau" in skills:
        return "Data Analyst"

    return "Data Science Enthusiast"