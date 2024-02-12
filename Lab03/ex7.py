import timeit
import json
import random
from matplotlib import pyplot as plt

def binary_search(arr, target, initial_midpoint=None):
   left = 0
   right = len(arr) - 1
   if initial_midpoint is None:
      midpoint = (left + right) // 2
   else:
      midpoint = initial_midpoint

   while left <= right:
      if arr[midpoint] == target:
         return midpoint
      elif arr[midpoint] < target:
         left = midpoint + 1
      else:
         right = midpoint - 1
      midpoint = (left + right) // 2
   return -1
   
# Import JSON files
with open('ex7data.json', 'r') as data_file:
   data = json.load(data_file)

with open('ex7tasks.json', 'r') as tasks_file:
   tasks = json.load(tasks_file)

best_midpoints = {}

for task in tasks:
   random_midpoints = [random.randint(0, len(data) - 1) for _ in range(100)]
   results = []

   for random_midpoint in random_midpoints:
      time_taken = timeit.timeit(lambda: binary_search(data, task, random_midpoint), number=100)
      avg_time = time_taken / 100
      results.append((random_midpoint, avg_time))

   # Find best midpoint with smallest average time
   best_midpoint, fastest = min(results, key=lambda x: x[1])
   best_midpoints[task] = best_midpoint

# Produce scatter plot with results
tasks_sorted, best_midpoints_sorted = zip(*sorted(best_midpoints.items()))

plt.figure(figsize=(10, 6))
plt.scatter(tasks_sorted, best_midpoints_sorted)
plt.xlabel("Tasks")
plt.ylabel("Best Midpoint")
plt.grid(True)
plt.show()


''' Q4. Based on the graph analysis, it appears that the proximity of the midpoint to the target value 
influences the speed of the search process. The graph suggests a linear trend, indicating that the most 
effective midpoint is near the actual target value. Consequently, when the initial midpoint is distant 
from the target value, the algorithm will have fewer values to divide during the first iteration, 
resulting in a longer search time. '''