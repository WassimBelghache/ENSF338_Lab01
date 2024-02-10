import json
import timeit
import matplotlib.pyplot as plt

INPUT_FILE = "large-file.json"
OUTPUT_FILE = "output.2.3.json"

def process_large_file():
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{INPUT_FILE}' not found.")
        return

    record_size = 1000
    subset_data = data[:record_size]

    timings = timeit.repeat(lambda: modify_size(subset_data), repeat=1000, number=1)

    plt.hist(timings, bins=20, edgecolor='black')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title(f'Distribution of Processing Time for {record_size} Records (1000 times)')
    plt.grid(True)
    plt.savefig('output.3.3.png')
    plt.show()

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        json.dump(data[::-1], file)

def modify_size(data_subset):
    for record in data_subset:
        record['size'] = 42

if __name__ == "__main__":
    process_large_file()
    