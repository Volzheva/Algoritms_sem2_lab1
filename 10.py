import time
import os, psutil


def eating_apples(apples, n, s):
    apples.sort(key=lambda a: [-(a[1] - a[0]), a[0]])
    j = 0
    psbl = True
    order = []
    while psbl and j < n:
        found = False
        a = 0
        while a < n and not found:
            if s - apples[a][0] > 0 and apples[a][2] != 0:
                found = True
                s += apples[a][1] - apples[a][0]
                order.append(apples[a][2])
                apples[a][2] = 0

            a += 1
        psbl = found
        j += 1
    if not psbl:
        order = []
    return order


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("input.txt")
m = open("output.txt", "w")
n, s = map(int, f.readline().split())
apples = []
for i in range(n):
    a, b = map(int, f.readline().split())
    apples.append([a, b, i + 1])

answer = eating_apples(apples, n, s)
if len(answer) == 0:
    m.write("-1")
else:
    for i in range(len(answer)):
        m.write(str(answer[i]) + ' ')
f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")