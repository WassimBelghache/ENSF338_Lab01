import json

def process_large_file():
    input_file = "large-file.json"
    output_file = "output.2.3.json"

    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for record in data:
        record['size'] = 42

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data[::-1], file)

if __name__ == "__main__":
    process_large_file()

