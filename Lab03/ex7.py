import timeit
import json
import random
from matplotlib import pyplot as plt

def binary_search(arr, key, midpoint=None):
   low = 0
   high = len(arr) - 1
   if midpoint is None:

      mid = (low + high) // 2
   else:
      mid = midpoint

   while low <= high:
      if arr[mid] == key:
         return mid
      elif arr[mid] < key:
         low = mid + 1
      else:
         high = mid -1
      mid = (low + high) // 2
   return -1
   
# import json files
with open('ex7data.json', 'r') as d:
   data = json.load(d)

with open('ex7tasks.json', 'r') as t:
   tasks = json.load(t)

best_midpoints = {}

for task in tasks:
   random_midpoints = [random.randint(0, len(data) - 1) for i in range(100)]
   results = []

   for random_midpoint in random_midpoints:
      time_taken = timeit.timeit(lambda: binary_search(data, task, random_midpoint), number=100)
      avg_time = time_taken/100
      results.append((random_midpoint, avg_time))

   # find best midpoint with one with smallest avg time
   best_midpoint, fastest = min(results, key=lambda x: x[1])
   best_midpoints[task] = best_midpoint

# produce scatter plot with results
tasks_sorted, best_midpoints_sorted = zip(*sorted(best_midpoints.items()))

plt.figure(figsize=(10, 6))
plt.scatter(tasks_sorted, best_midpoints_sorted)
plt.xlabel("tasks")
plt.ylabel("best midpoint")
plt.grid(True)
plt.show()

''' Q4. Based on the graph analysis, it appears that the proximity of the midpoint to the target value 
influences the speed of the search process. The graph suggests a linear trend, indicating that the most 
effective midpoint is near the actual target value. Consequently, when the initial midpoint is distant 
from the target value, the algorithm will have fewer values to divide during the first iteration, 
resulting in a longer search time. '''