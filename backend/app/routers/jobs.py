from fastapi import APIRouter
from app.database import jobs_collection

router = APIRouter(
    prefix="/api/jobs",
    tags=["Jobs"]
)


@router.get("/")
def get_jobs():

    jobs = list(
        jobs_collection.find(
            {},
            {"_id": 0}
        )
    )

    return {
        "success": True,
        "data": jobs
    }


@router.post("/")
def create_job(job: dict):

    result = jobs_collection.insert_one(job)

    return {
        "success": True,
        "message": "Job created successfully",
        "id": str(result.inserted_id)
    }