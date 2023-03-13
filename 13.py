import time
import os, psutil


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("input.txt")
m = open("output.txt", "w")
n = int(f.readline())
numbers = list(map(int, f.readline().split()))

res = 1
if sum(numbers) % 3 == 0:
    third_part = sum(numbers) / 3
    numbers.sort()
    numbers.reverse()
    for i in range(3):
        part = []
        j = 0
        while sum(part) != third_part:
            if j > len(numbers)-1:
                res = 0
                break
            if (sum(part) + numbers[j]) <= third_part:
                part.append(numbers[j])
                del(numbers[j])
            else:
                j += 1
        if j > len(numbers) - 1:
            break
else:
    res = 0

if res == 1:
    res = 1
    if sum(numbers) % 2 == 0:
        half_sum = sum(numbers) / 2
        numbers.sort()
        numbers.reverse()
        part = []
        j = 0
        while sum(part) != half_sum:
            if j > len(numbers) - 1:
                res = 0
                break
            if (sum(part) + numbers[j]) <= half_sum:
                part.append(numbers[j])
                del (numbers[j])
            else:
                j += 1
    else:
        res = 0

m.write(str(res))
f.close()
m.close()
print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")