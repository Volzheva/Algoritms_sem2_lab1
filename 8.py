import time
import os, psutil
from operator import itemgetter


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("input.txt")
m = open("output.txt", "w")
n = int(f.readline())
a = []
for i in range(n):
    data = f.readline()
    a.append([int(data.split()[0]), int(data.split()[1])])

a.sort(key=itemgetter(1))

end = 0
count = 0
for i in range(n):
    if a[i][0] >= end:
        end = a[i][1]
        count += 1

m.write(str(count))
f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")