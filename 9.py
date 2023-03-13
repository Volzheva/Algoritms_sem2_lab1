import time
import os, psutil
from operator import itemgetter


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("input.txt")
m = open("output.txt", "w")

n = int(f.readline())
a = []
for i in range(7):
    data = f.readline()
    a.append(int(data))

for i in range(1, 7):
    a[i] = min(a[i], a[i-1]*10)
    print(a)

current = 0
result = 0
copy_n = n

while copy_n > 0:
    result += a[current]*(copy_n % 10)
    copy_n //= 10
    current += 1

power = 1
for i in range(7):
    if power >= n and a[i] < result:
        result = a[i]
    power *= 10

m.write(str(result))
f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")