def calculate_average(grades):
    avg_marks = {}
    for student, scores in grades.items():
        avg_marks[student] = round(sum(scores) / len(scores), 2)
    return avg_marks


def find_topper(avg_marks):
    topper = max(avg_marks, key=avg_marks.get)
    return topper


students_scores = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

averages = calculate_average(students_scores)
topper = find_topper(averages)

print("Average Marks:", averages)
print("Top Performer:", topper)
