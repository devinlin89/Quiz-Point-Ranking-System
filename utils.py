def format_subject_quiz_name(input_string):
    # Create a dictionary mapping subject abbreviations to full names
    subject_mapping = {
        "bio": "Biology",
        "chem": "Chemistry",
        "phy": "Physics",
    }

    # Split the input string into parts using "_" as the separator
    parts = input_string.split("_")

    # Check if the first part (subject abbreviation) is in the dictionary
    if parts[0] in subject_mapping:
        # If it's in the dictionary, replace it with the full name
        parts[0] = subject_mapping[parts[0]] + " Quiz"

    # Join the parts back together with spaces
    result = " ".join(parts)

    return result