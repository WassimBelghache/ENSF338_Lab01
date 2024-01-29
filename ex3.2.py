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

    record_sizes = [1000, 2000, 5000, 10000]
    average_times = []

    for size in record_sizes:
        subset_data = data[:size]
        total_time = timeit.timeit(lambda: modify_size(subset_data), number=100)
        average_time = total_time / 100
        average_times.append(average_time)
        print(f'Average time for {size} records: {average_time:.6f} seconds')

    generate_regression_plot(record_sizes, average_times)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        json.dump(data[::-1], file)

def modify_size(data_subset):
    for record in data_subset:
        record['size'] = 42

def generate_regression_plot(record_sizes, average_times):
    plt.plot(record_sizes, average_times, 'o-', label='Average Time')
    plt.xlabel('Number of Records')
    plt.ylabel('Average Processing Time (seconds)')
    plt.title('Processing Time vs Number of Records')
    plt.legend()
    plt.grid(True)
    plt.savefig('output.3.2.png')
    plt.show()

if __name__ == "__main__":
    process_large_file()