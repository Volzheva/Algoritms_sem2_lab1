import time
import os, psutil


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("input.txt")
m = open("output.txt", "w")
n = int(f.readline())
numbers = list(map(int, f.readline().split()))

res = 0
if sum(numbers) % 2 == 0:
    half_sum = sum(numbers) / 2
    numbers.sort()
    numbers.reverse()
    part = []
    j = 0
    while sum(part) != half_sum:
        if j > len(numbers) - 1:
            res = -1
            break
        if (sum(part) + numbers[j]) <= half_sum:
            part.append(numbers[j])
            del (numbers[j])
        else:
            j += 1
else:
    res = -1

if res == -1:
    m.write('-1')
else:
    m.write(str(len(part))+'\n')
    m.write(' '.join(map(str, part)))


f.close()
m.close()
print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")