import json
import random
from app.config import DATA_PATH

def load_questions():
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def generate_question(role):
    questions = load_questions()
    if role not in questions:
        return None
    return random.choice(questions[role])
