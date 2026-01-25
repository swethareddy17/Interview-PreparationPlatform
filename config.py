import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATA_PATH = os.path.join(BASE_DIR, "..", "data", "role_questions.json")

SECRET_KEY = "interview_platform_key"
