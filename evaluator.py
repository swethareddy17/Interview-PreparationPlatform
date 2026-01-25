from core.text_processing import preprocess_text

def evaluate_answer(answer, keywords):
    tokens = preprocess_text(answer)
    matched = sum(1 for k in keywords if k.lower() in tokens)
    score = int((matched / len(keywords)) * 100)
    return score, matched
