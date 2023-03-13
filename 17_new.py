import time
import os, psutil


def horse(n):
    button = [0] * 10
    if n == 1:
        return 8
    else:
        button = [2, 1, 2, 1, 2, 0, 2, 2, 2, 2]
        arr = [0] * 10
        for i in range(n - 2):
            arr[0] = button[4] + button[6]
            arr[1] = button[6] + button[8]
            arr[2] = button[7] + button[9]
            arr[3] = button[4] + button[8]
            arr[4] = button[0] + button[3] + button[9]
            arr[5] = 0
            arr[6] = button[0] + button[1] + button[7]
            arr[7] = button[2] + button[6]
            arr[8] = button[1] + button[3]
            arr[9] = button[2] + button[4]
            button = arr
            arr = [0] * 10

    return sum(button) % 10**9


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("input.txt")
m = open("output.txt", "w")
number = int(f.readline())
m.write(str(horse(number)))
f.close()
m.close()
print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")