def recommend_jobs(skills):

    jobs = []

    if "Python" in skills:
        jobs.append("Data Scientist")

    if "Machine Learning" in skills:
        jobs.append("Machine Learning Engineer")

    if "SQL" in skills:
        jobs.append("Data Analyst")

    if "Deep Learning" in skills:
        jobs.append("AI Engineer")

    if not jobs:
        jobs.append("Junior Data Analyst")

    return jobs