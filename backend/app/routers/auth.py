from fastapi import APIRouter

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login(data: dict):

    email = data.get("email")
    password = data.get("password")

    return {
        "success": True,
        "message": "Login API connected",
        "email": email
    }