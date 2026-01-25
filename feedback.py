def generate_feedback(score):
    if score >= 80:
        return "Excellent answer! You covered all key points."
    elif score >= 50:
        return "Good effort, but you missed some important keywords."
    else:
        return "Keep practicing. Your answer was a bit off."
