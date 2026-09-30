from fastapi import APIRouter
from app.database import (
    students_collection,
    jobs_collection,
    applications_collection
)

router = APIRouter(
    prefix="/api/analytics",
    tags=["Analytics"]
)


@router.get("/")
def get_analytics():

    return {
        "students": students_collection.count_documents({}),
        "jobs": jobs_collection.count_documents({}),
        "applications": applications_collection.count_documents({})
    }