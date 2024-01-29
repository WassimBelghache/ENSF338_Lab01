import json
import timeit

def process_large_file():
    input_file = "large-file.json"
    output_file = "output.2.3.json"

    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    def modify_size():
        for record in data:
            record['size'] = 42
    
    total_time = timeit.timeit(modify_size, number=10)
    
    average_time = total_time / 10
    print(f'average time across 10 repetitions: {average_time:.6f} seconds')

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data[::-1], file)

if __name__ == "__main__":
    process_large_file()