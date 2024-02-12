import random
import time
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def measure_performance(search_func, input_size):
    total_time = 0
    for _ in range(100):
        arr = list(range(1, input_size + 1))  # Generate a sorted array
        target = random.randint(1, input_size)
        start_time = time.time()
        search_func(arr, target)
        end_time = time.time()
        total_time += end_time - start_time
    return total_time / 100

input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
linear_search_times = []
binary_search_times = []

for size in input_sizes:
    linear_time = measure_performance(linear_search, size)
    binary_time = measure_performance(binary_search, size)
    linear_search_times.append(linear_time)
    binary_search_times.append(binary_time)
    print(f"Input size: {size}, Linear search time: {linear_time}, Binary search time: {binary_time}")

plt.plot(input_sizes, linear_search_times, label='Linear Search')
plt.plot(input_sizes, binary_search_times, label='Binary Search with Quicksort (Worst-case)')
plt.xlabel('Input Size')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Performance Comparison: Linear Search vs Binary Search with Quicksort (Worst-case)')
plt.legend()
plt.show()

# question 4 ans:
# similarly to the average case, in worst case binary search is shown to be quicker than Linear search, both in the outputed time data and the graph.