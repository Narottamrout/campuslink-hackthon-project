from fastapi import APIRouter
from app.database import students_collection, jobs_collection

router = APIRouter(
    prefix="/api/matching",
    tags=["Matching"]
)


@router.get("/{student_name}")
def match_jobs(student_name: str):

    student = students_collection.find_one({
        "name": student_name
    })

    if not student:
        return {
            "success": False,
            "message": "Student not found"
        }

    student_skills = set(
        skill.lower()
        for skill in student.get("skills", [])
    )

    jobs = list(jobs_collection.find())

    results = []

    for job in jobs:

        required_skills = set(
            skill.lower()
            for skill in job.get("required_skills", [])
        )

        if not required_skills:
            score = 0
        else:
            matched = student_skills.intersection(
                required_skills
            )

            score = (
                len(matched)
                / len(required_skills)
            ) * 100

        results.append({
            "company": job.get("company"),
            "title": job.get("title"),
            "location": job.get("location"),
            "match_percentage": round(score, 2)
        })

    results.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    return {
        "success": True,
        "student": student_name,
        "matches": results
    }