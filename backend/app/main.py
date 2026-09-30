# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from app.routers import jobs


# app = FastAPI(
#     title="CampusLink API",
#     description="Backend API for CampusLink",
#     version="1.0.0"
# )


# # CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:5173",
#         "http://127.0.0.1:5173"
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# # Job API
# app.include_router(jobs.router)



# @app.get("/")
# def root():
#     return {
#         "message": "CampusLink Backend Running Successfully 🚀"
#     }


# @app.get("/api/health")
# def health():
#     return {
#         "status": "healthy",
#         "backend": "FastAPI",
#         "database": "MongoDB"
#     }
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    auth,
    students,
    jobs,
    matching,
    analytics
)


app = FastAPI(
    title="CampusLink API",
    description="Backend API for CampusLink",
    version="1.0.0"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
app.include_router(auth.router)
app.include_router(students.router)
app.include_router(jobs.router)
app.include_router(matching.router)
app.include_router(analytics.router)


@app.get("/")
def root():

    return {
        "message": "CampusLink Backend Running Successfully 🚀"
    }


@app.get("/api/health")
def health():

    return {
        "status": "healthy",
        "backend": "FastAPI",
        "database": "MongoDB"
    }