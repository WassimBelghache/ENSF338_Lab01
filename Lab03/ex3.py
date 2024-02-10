
#Bubble sort that counts comparisons and swaps
def bubble_sort(arr):
	swaps = 0
	comparisons = 0
	n = len(arr)
	
	for i in range(n):
		for j in range(0, n-i-1):
			comparisons += 1
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
				swaps += 1
	return swaps, comparisons