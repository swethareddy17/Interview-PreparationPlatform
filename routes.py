from flask import Blueprint, render_template, request, redirect, url_for
from question_generator import generate_question
from evaluator import evaluate_answer
from feedback import generate_feedback
from results import save_result

main = Blueprint("main", __name__)

current_question = {}
score_history = []

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        role = request.form["role"]

        current_question["role"] = role
        score_history.clear()

        return redirect(url_for("main.interview"))

    return render_template("index.html")


@main.route("/interview")
def interview():
    role = current_question.get("role")

    question = generate_question(role)

    if not question:
        return render_template("index.html", error="Invalid role")

    current_question["data"] = question

    return render_template("interview.html", question=question["question"])


@main.route("/submit", methods=["POST"])
def submit():
    answer = request.form["answer"]
    question_data = current_question["data"]

    score, _ = evaluate_answer(answer, question_data["keywords"])
    feedback = generate_feedback(score)

    score_history.append(score)

    return render_template(
        "interview.html",
        question=generate_question(current_question["role"])["question"],
        feedback=feedback,
        score=score
    )


@main.route("/quit")
def quit():
    avg_score = sum(score_history) / len(score_history) if score_history else 0

    save_result(current_question["role"], "Multiple Questions", avg_score)

    return render_template("result.html", score=avg_score, feedback="Interview Ended")