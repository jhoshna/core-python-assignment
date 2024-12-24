def positive_feedback(scores):
    if not scores:
        return 0.0
    positive = sum(1 for score in scores if score >= 4)
    return round((positive / len(scores)) * 100, 2)


scores = [5, 4, 3, 5, 2, 4, 1, 5]

percent = positive_feedback(scores)

print(f"Positive Feedback:{percent}%")