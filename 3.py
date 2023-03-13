import time
import os, psutil


def decision(count, values, weights):
    total = 0
    values.sort()
    weights.sort()
    for i in range(count):
        total += values[i] * weights[i]
    return total


process = psutil.Process(os.getpid())
t_start = time.perf_counter()
f = open("input.txt")
m = open("output.txt", "w")
count = int(f.readline())
values = list(map(int, f.readline().split()))
weights = list(map(int, f.readline().split()))
m.write(str(decision(count, values, weights)))
f.close()
m.close()
print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")