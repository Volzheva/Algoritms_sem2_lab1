import time
import os, psutil


def decision(minutes, all_minutes):
    minutes = sorted(minutes)
    sum_minutes = 0
    counts = 0
    for i in minutes:
        sum_minutes += i
        if sum_minutes <= all_minutes:
            counts += 1
        else:
            break
    return counts


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("input.txt")
m = open("output.txt", "w")
all_minutes, shoes = map(int, f.readline().split())
minutes = list(map(int, f.readline().split()))
minutes = sorted(minutes)
count_shoes = decision(minutes, all_minutes)
m.write(str(count_shoes))
f.close()
m.close()
print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")