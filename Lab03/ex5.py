import timeit
import random 
import numpy as np
from matplotlib import pyplot as plt
import scipy

# 'Traditional' Insertion Sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#Binary Search used for BinaryInsertionSort
def binarySearch(Array, N, key):
    L = 0
    R = N
    while(L < R):
        mid = (L + R)//2
        if (Array[mid] <= key):
            L = mid + 1
        else:
            R = mid - 1
    return L

#BinaryInsertionSort
def binaryInsertionSort(Array):
    for i in range (1,len(Array)):
        key = Array[i]
        position = binarySearch(Array, i, key)
        j = i

        while(j > position):
            Array[j] = Array[j-1]
            j = j-1

        Array[position] = key

def func(x, a, b):
    return a * np.square(x) + b

SIZE_LIST = range(100, 1001, 100)
numofruns = 100  

binaryInsertion = []
insertion = []

#Testing binary Insertion Sorting algorithm with small but increasing input size
for arr in SIZE_LIST:

    insertionTime = 0
    binaryInsertionTime = 0

    for iterations in range(numofruns):
        randList = random.sample(range(0, arr), arr)
        copyOfRandList = randList.copy()
        insertionTime += timeit.timeit(lambda: insertionSort(randList), number=1)
        binaryInsertionTime += timeit.timeit(lambda: binaryInsertionSort(copyOfRandList), number=1)
    binaryInsertion.append(binaryInsertionTime)
    insertion.append(insertionTime)

avg_binary_insertion = []
avg_insertion_list = []
for i in range(len(SIZE_LIST)):
    avg_binary_insertion.append(binaryInsertion[i] / numofruns)
    avg_insertion_list.append(insertion[i] / numofruns)

popt, pcov = scipy.optimize.curve_fit(func, SIZE_LIST, avg_insertion_list)
popt2, pcov2 = scipy.optimize.curve_fit(func, SIZE_LIST, avg_binary_insertion)

# Plotting the data and the fitted curve
plt.scatter(SIZE_LIST, avg_insertion_list, label='Insertion Sort')
plt.scatter(SIZE_LIST, avg_binary_insertion, label='Binary Insertion Sort')

# Plot the fitted curve
x_values = np.linspace(min(SIZE_LIST), max(SIZE_LIST), 100)
fitted_curve = func(x_values, *popt)
fitted_curve2 = func(x_values, *popt2)

plt.plot(x_values, fitted_curve, 'b')
plt.plot(x_values, fitted_curve2, 'black')
plt.xlabel('Input Sizes')
plt.ylabel('Average Time (s)')
plt.legend()
plt.savefig("5.3.jpg")


'''
Q4

Binary insertion sort is faster than insertion sort. Binary insertion sort typically performs 
fewer comparisons than traditional insertion sort. In traditional insertion sort, the algorithm 
compares the current element with each element in the sorted portion until it finds the correct position, 
which can result in more comparisons, especially for larger lists. Binary search has a time 
complexity of O(log n), whereas linear search has a time complexity of O(n). By using binary 
search in the insertion step, binary insertion sort reduces the time complexity of finding the 
correct position for each element, leading to overall faster performance, especially for large lists.
'''