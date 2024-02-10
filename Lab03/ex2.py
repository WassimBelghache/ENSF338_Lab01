import timeit
import random
from matplotlib import pyplot as plt
def bubbleSort(a,len):
    for y in range(len-1):
        swaps = False
        for x in range (len-1-y):
            if a[x] > a[x+1]:
                swaps = True
                (a[x],a[x+1]) = (a[x+1],a[x])
        if swaps == False:
            break
def partition(a,low,high):
    pivot = a[high]
    i = low-1
    for x in range(low,high):
        if a[x] <= pivot:
            i = i+1
            (a[i],a[x]) = (a[x], a[i])
    (a[i+1],a[high]) = (a[high],a[i+1])
    return i+1
def quickSort(a,low,high):
    if low<high:
        part = partition(a,low,high)
        quickSort(a,low,part-1)
        quickSort(a,part+1,high)
bestBubble = []
worstBubble = []
averageBubble = []
worstQuick = []
averageQuick = []
choices = [2,4,6,8,10,12,14,16,18,20,25,30,35,40,45,50,75,100,125,150]
for x in range(20):
    test1 = [y for y in range(choices[x])]
    bestBubble.append(timeit.timeit(lambda: bubbleSort(test1,len(test1)), number=1))
    test1 = [choices[x] - y for y in range(choices[x])]
    test2 = [choices[x] - y for y in range(choices[x])]
    worstBubble.append(timeit.timeit(lambda: bubbleSort(test1,len(test1)), number=1))
    worstQuick.append(timeit.timeit(lambda: quickSort(test2,0,len(test2)-1), number=1))
    test1 = random.sample(range(0,1000),choices[x])
    test2 = random.sample(range(0,1000),choices[x])
    averageBubble.append(timeit.timeit(lambda: bubbleSort(test1,len(test1)), number=1))
    averageQuick.append(timeit.timeit(lambda: quickSort(test2,0,len(test2)-1), number=1))
plt.scatter(choices,bestBubble,color = 'blue')
plt.scatter(choices,averageQuick,color = 'red')
plt.xlabel("length of array sorted")
plt.ylabel("Time elapsed")
plt.title("Comparison of Bubble and Quick sort best cases")
plt.legend(["Bubble","Quick"])
plt.savefig("ex2.bestCases.png")
plt.clf()
plt.scatter(choices,averageBubble,color = 'blue')
plt.scatter(choices,averageQuick,color = 'red')
plt.xlabel("length of array sorted")
plt.ylabel("Time elapsed")
plt.title("Comparison of Bubble and Quick sort average cases")
plt.legend(["Bubble","Quick"])
plt.savefig("ex2.averageCases.png")
plt.clf()
plt.scatter(choices,worstBubble,color = 'blue')
plt.scatter(choices,worstQuick,color = 'red')
plt.xlabel("length of array sorted")
plt.ylabel("Time elapsed")
plt.title("Comparison of Bubble and Quick sort worst cases")
plt.legend(["Bubble","Quick"])
plt.savefig("ex2.worstCases.png")
plt.clf()