import time
import os, psutil


def decision(my_distance, stops):
    stops_new = []
    stops_new.append(stops[0])
    for i in range(1, len(stops)):
        stops_new.append(stops[i] - stops[i-1])
    sum = 0
    count = 0
    for i in stops_new:
        sum += i
        if sum > my_distance:
            count += 1
            sum = i
        if i > my_distance:
            return -1
    return count


process = psutil.Process(os.getpid())
t_start = time.perf_counter()
f = open("input.txt")
m = open("output.txt", "w")
all_distance = int(f.readline())
my_distance = int(f.readline())
count = int(f.readline())
stops = list(map(int, f.readline().split()))
stops.append(all_distance)
count_necessary_stops = decision(my_distance, stops)
m.write(str(count_necessary_stops))
f.close()
m.close()
print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
