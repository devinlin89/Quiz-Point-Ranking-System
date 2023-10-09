from open_json import open_json
from utils import format_subject_quiz_name

CMA = open_json("config")["CMA"]

points = open_json("config")["points"]

student_lst = open_json("config")["students"]
student_points_dict = {item: 0 for item in student_lst}
print(student_points_dict)

quizzes = open_json("quizzes")

for quiz in quizzes:
    print(f"# {format_subject_quiz_name(quiz)}")
    print(" ")

    current_quiz_scores = open_json(quiz)
    sorted_quiz_scores = sorted(current_quiz_scores.items(), key=lambda x: x[1], reverse=True)

    # Quiz Rankings
    print("## Quiz Rankings")
    print(" ")
    sorted_students = [student[0] for student in sorted_quiz_scores]

    # Loop through every student to print out the rankings
    for count, student in enumerate(sorted_students, start=1):
        print(f"{count}. {student}")

    print(" ")

    # Finds students that received scores above 75
    filtered_students = [student for student in sorted_students if current_quiz_scores.get(student, 0) >= CMA]

    # Students who receive scores above 75 and are within the top 5
    # will receive points according to the point rules in config.json
    print("## Points Gained")
    print(" ")

    new_points = dict(zip(filtered_students, points))

    count = 1

    for student, points_gained in new_points.items():
        print(f"{count}. {student}: {points_gained}")
        count += 1

    print(" ")

    # Adds the new points gained into the original point value of all students
    print("## Championship Standings")
    print(" ")

    for student, points_gained in new_points.items():
        student_points_dict[student] += points_gained

    # Loops through all students to print the championship standings
    count = 1

    for key, value in student_points_dict.items():
        print(f"{count}. {key}: {value}")
        count += 1

    print(" ")

