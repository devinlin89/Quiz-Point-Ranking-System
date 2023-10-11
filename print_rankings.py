def print_quiz_rankings(sorted_students):
    print("## Quiz Rankings")
    for count, student in enumerate(sorted_students, start=1):
        print(f"{count}. {student}")
    print()

def print_points_gained(new_points):
    print("## Points Gained")

    # Calculates the amount of points gained by every student
    for count, (student, points_gained) in enumerate(new_points.items(), start=1):
        print(f"{count}. {student}: {points_gained}")
    print()

def update_championship_standings(student_points_dict, new_points):
    # Loops through every student to add the points that they have gained
    for student, points_gained in new_points.items():
        student_points_dict[student] += points_gained

    # Sort the dictionary by values (points)
    sorted_standings = dict(sorted(student_points_dict.items(), key=lambda item: item[1], reverse=True))

    print("## Championship Standings")

    # Loops through every student to print out their championship standings
    for count, (student, points) in enumerate(sorted_standings.items(), start=1):
        print(f"{count}. {student}: {points}")
    print()