# from fastapi import APIRouter
# from app.database import students_collection

# router = APIRouter(
#     prefix="/api/students",
#     tags=["Students"]
# )


# @router.get("/")
# def get_students():
#     students = list(
#         students_collection.find(
#             {},
#             {"_id": 0}
#         )
#     )

#     return {
#         "success": True,
#         "data": students
#     }


# @router.post("/")
# def create_student(student: dict):

#     result = students_collection.insert_one(student)

#     return {
#         "success": True,
#         "message": "Student created",
#         "id": str(result.inserted_id)
#     }
from fastapi import APIRouter
from app.database import students_collection

router = APIRouter(
    prefix="/api/students",
    tags=["Students"]
)


@router.get("/")
def get_students():

    students = list(
        students_collection.find(
            {},
            {"_id": 0}
        )
    )

    return {
        "success": True,
        "data": students
    }


@router.post("/")
def create_student(student: dict):

    result = students_collection.insert_one(student)

    return {
        "success": True,
        "message": "Student created successfully",
        "id": str(result.inserted_id)
    }