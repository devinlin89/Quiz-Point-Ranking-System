import json

def open_json(name: str):
    file = f'quiz_scores/{name}.json'

    with open(file, 'r') as open_file:
        return json.load(open_file)