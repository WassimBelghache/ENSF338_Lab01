import math
import timeit 

def pow2(n):
    return 2 ** n

total_time = timeit.timeit(lambda: pow2(10000), number = 100000)
average_time = total_time / 10000
print(f'average time: {average_time:.6f} seconds')

def pow2_loop(n):
    result = []
    for i in range(n):
        result.append(pow2(i))
    return result

total_loop_time = timeit.timeit(lambda: pow2_loop(1000), number=1000)
average_loop_time = total_loop_time / 1000
print(f'average loop time: {average_loop_time:.6f} seconds')

def pow2_list_comprehension(n):
    return [pow2(i) for i in range(n)]

#'LC' for list comprehension
total_LC_time = timeit.timeit(lambda: pow2_list_comprehension(1000), number=1000)
average_LC_time = total_LC_time / 1000
print(f'average isntance time: {average_LC_time:.6f} seconds')