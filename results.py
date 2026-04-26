import json
import os
from config import BASE_DIR

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_FILE = os.path.join(BASE_DIR, "results.json")

def save_result(role, question, score):
    result_data = {
        "role": role,
        "question": question,
        "score": score
    }

    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r") as f:
            try:
                results = json.load(f)
            except json.JSONDecodeError:
                results = []
    else:
        results = []

    results.append(result_data)

    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=4)
