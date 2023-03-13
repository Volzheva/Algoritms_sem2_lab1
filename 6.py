import time
import os, psutil
import math


def bubble_sort(n, arr):
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            x = arr[j] + arr[j + 1]
            y = arr[j + 1] + arr[j]
            if x < y:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    res = ''
    for i in range(0, n):
        res += str(int(arr[i]))
    return res


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("input.txt")
m = open("output.txt", "w")
number = int(f.readline())
source_array = f.readline().split(' ')
print(bubble_sort(number, source_array))
m.write(bubble_sort(number, source_array))
f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
