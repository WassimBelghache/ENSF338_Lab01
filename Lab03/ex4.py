import random
import matplotlib.pyplot as plt
import numpy as np
import timeit

def quicksort(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    quicksort(arr, low, pi - 1)
    quicksort(arr, pi + 1, high)

def partition(arr, low, high):
  pivot = arr[high] 
  i = (low - 1) 
  for j in range(low, high):

    if arr[j] <= pivot:
      i = i + 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1

def measure_time(n):
  arr = random.sample(range(1, n + 1), n)

  start_time = timeit.default_timer()
  quicksort(arr, 0, len(arr) - 1)
  end_time = timeit.default_timer()
  return end_time - start_time

n_values = range(100, 1001, 100)
time_values = [measure_time(n) for n in n_values]

plt.plot(n_values, time_values, 'o', label='Quicksort (worst-case)')

quadratic_fit = np.polyfit(n_values, time_values, 2)

plt.plot(n_values, np.polyval(quadratic_fit, n_values), label='Quadratic fit')
plt.plot(n_values, [n**2 for n in n_values], label='O(n^2)')
plt.xlabel('Array size (n)')
plt.ylabel('Execution time (seconds)')
plt.title('Worst-case complexity of quicksort')
plt.legend()
plt.show()