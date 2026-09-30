import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb://localhost:27017"
)

DATABASE_NAME = os.getenv(
    "DATABASE_NAME",
    "campuslink"
)

client = MongoClient(MONGO_URL)

db = client[DATABASE_NAME]

students_collection = db["students"]
jobs_collection = db["jobs"]
recruiters_collection = db["recruiters"]
applications_collection = db["applications"]
skills_collection = db["skills"]
learning_paths_collection = db["learning_paths"]
match_results_collection = db["match_results"]
analytics_collection = db["analytics"]