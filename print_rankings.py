def print_quiz_rankings(sorted_students):
    print("## Quiz Rankings")
    for count, student in enumerate(sorted_students, start=1):
        print(f"{count}. {student}")
    print()

def print_points_gained(new_points):
    print("## Points Gained")
    for count, (student, points_gained) in enumerate(new_points.items(), start=1):
        print(f"{count}. {student}: {points_gained}")
    print()

def update_championship_standings(student_points_dict, new_points):
    for student, points_gained in new_points.items():
        student_points_dict[student] += points_gained

def print_championship_standings(student_points_dict):
    print("## Championship Standings")
    for count, (student, points) in enumerate(student_points_dict.items(), start=1):
        print(f"{count}. {student}: {points}")
    print()