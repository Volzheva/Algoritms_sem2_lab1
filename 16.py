import time
import os, psutil
import math


def find_right_way(arr, n):
    visited_cities = [False] * n
    lengths = [math.inf] * n
    result = [None] * n
    current = 0
    lengths[current] = 0
    for i in range(0, n):
        min_path_length = float('inf')
        for j in range(0, n):
            if not visited_cities[j] and lengths[j] < min_path_length:
                min_path_length = lengths[j]
                current = j
        visited_cities[current] = True
        result[current] = i + 1
        for j in range(0, n):
            if not visited_cities[j] and arr[current][j] < lengths[j]:
                lengths[j] = arr[current][j]
    return sum(lengths), reversed(result)


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("input.txt")
m = open("output.txt", "w")

n = int(f.readline())
roads = [list(map(int, f.readline().split())) for i in range(n)]

lenght, order = find_right_way(roads, n)
m.write(str(lenght) + "\n")
for i in order:
    m.write(str(i) + " ")

f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")