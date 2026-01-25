from flask import Blueprint, render_template, request
from core.question_generator import generate_question
from core.evaluator import evaluate_answer
from core.feedback import generate_feedback
from storage.results import save_result

main = Blueprint("main", __name__)

current_question = {}

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        role = request.form["role"]
        question = generate_question(role)

        if not question:
            return render_template("index.html", error="Invalid role")

        current_question["role"] = role
        current_question["data"] = question

        return render_template("interview.html", question=question["question"])

    return render_template("index.html")
    

@main.route("/submit", methods=["POST"])
def submit():
    answer = request.form["answer"]
    question_data = current_question["data"]

    score, _ = evaluate_answer(answer, question_data["keywords"])
    feedback = generate_feedback(score)

    save_result(current_question["role"], question_data["question"], score)

    return render_template(
        "result.html",
        score=score,
        feedback=feedback
    )
