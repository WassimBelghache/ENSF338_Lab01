import matplotlib.pyplot as plt
from random import randint


#Bubble sort that counts comparisons and swaps
def bubble_sort(arr):
	n = len(arr)
	
	for i in range(n):
		global swaps
		global comparisons
		for j in range(0, n-i-1):
			comparisons += 1
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
				swaps += 1
	return arr

nums = [1000, 2000, 4000, 8000, 16000, 32000]
comp = []
swap = []

arr1000 = [randint(1, 1000) for i in range(1000)]

arr2000 = [randint(1, 2000) for i in range(2000)]

arr4000 = [randint(1, 4000) for i in range(4000)]

arr8000 = [randint(1, 8000) for i in range(8000)]

swaps = 0
comparisons = 0

bubble_sort(arr1000)

comp.append(comparisons)
swap.append(swaps)

comparisons = 0
swaps = 0

bubble_sort(arr2000)

comp.append(comparisons)
swap.append(swaps)

comparisons = 0
swaps = 0

bubble_sort(arr4000)

comp.append(comparisons)
swap.append(swaps)

comparisons = 0
swaps = 0

bubble_sort(arr8000)

comp.append(comparisons)
swap.append(swaps)

comparisons = 0
swaps = 0

plt.scatter(nums,comp)
plt.xlabel("Number of Elements")
plt.ylabel("Number of Comparisons")
plt.title("Comparisons vs Elements")
plt.savefig("ex3.comparisonsVsElements.png")
plt.clf()
plt.scatter(nums,swap)
plt.xlabel("Number of Elements")
plt.ylabel("Number of Swaps")
plt.title("Swaps vs Elements")
plt.savefig("ex3.swapsVsElements.png")
plt.clf()