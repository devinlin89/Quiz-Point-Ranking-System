from open_json import open_json
from print_rankings import *

def format_subject_quiz_name(input_string):
    # Create a dictionary mapping subject abbreviations to full names
    subject_mapping = open_json("config")["subject_mapping"]

    # Split the input string into parts at "_"
    parts = input_string.split("_")

    # Check if the first part (subject abbreviation) is in the dictionary
    if parts[0] in subject_mapping:
        # If it's in the dictionary, replace it with the full name
        parts[0] = subject_mapping[parts[0]] + " Quiz"

    # Join the parts back together with spaces
    result = " ".join(parts)

    return result

def load_config():
    # Loads all the config variables

    config = open_json("config")
    CMA = config["CMA"]
    points_distribution = config["points_distribution"]
    students = config["students"]
    quiz_folder = config["quiz_folder"]

    return CMA, points_distribution, students, quiz_folder

def load_quiz_data(quiz_folder, quiz):
    file_path = f"{quiz_folder}/{quiz}"

    return open_json(file_path)

def load_quiz_list(quiz_folder):
    file_path = f"{quiz_folder}/list_quizzes"

    return open_json(file_path)


def find_keys_with_duplicate_values(d, points_dict):
    value_to_keys = {}
    duplicates = []

    for key, value in d.items():
        if value in value_to_keys:
            value_to_keys[value].append(key)
        else:
            value_to_keys[value] = [key]

    for value, keys in value_to_keys.items():
        if len(keys) > 1:
            duplicates.extend(keys)

    # Sort the duplicates based on points from the points_dict
    duplicates.sort(key=lambda key: points_dict[key])

    return duplicates


def main():
    # Loads in global variables from config.json
    CMA, points_distribution, students, quiz_folder = load_config()

    # Creates an empty student points dictionary in the form of "student: 0"
    student_points_dict = {item: 0 for item in students}

    # Gets quiz list from quizzes.json
    quizzes = load_quiz_list(quiz_folder)

    for quiz in quizzes:
        # Loops through all quizzes in the quizzes list and does the following things:
        # 1. Find and print quiz rankings
        # 2. Find and print points gained
        # 3. Print new championship standings

        # Formats and prints current quiz name
        print(f"# {format_subject_quiz_name(quiz)}\n")

        # Loads in the scores from the current quiz.json
        current_quiz_scores = load_quiz_data(quiz_folder, quiz)

        # Converts the dictionary into a list of tuples from highest to lowest
        sorted_quiz_scores = sorted(current_quiz_scores.items(), key=lambda x: x[1], reverse=True)

        # Creates list of quiz rankings and prints it out
        sorted_students = []

        # Loop through each student in sorted_quiz_scores and sort using the sorting_key function

        students_same_score = find_keys_with_duplicate_values(current_quiz_scores, student_points_dict)

        for student_score in sorted(sorted_quiz_scores):
            student = student_score[0]

            sorted_students.append(student)

        sorted_students = sorted(sorted_students, key=lambda x: students_same_score.index(x) if x in students_same_score else len(students_same_score))

        print_quiz_rankings(sorted_students)

        # Creates list of students which get above CMA (75 in this case)
        filtered_students = [student for student in sorted_students if current_quiz_scores.get(student, 0) >= CMA]

        # Point rules:
        # 1. Student must have a score above 75 to gain points
        # 2. Students must be in the top 6 to gain points
        # according to the distribution in config.json
        print_points_gained(dict(zip(filtered_students, points_distribution)))

        # Sums the points gained in the quiz with current total points and prints it out
        update_championship_standings(student_points_dict, dict(zip(filtered_students, points_distribution)))

if __name__ == "__main__":
    main()