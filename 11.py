import time
import os, psutil


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("input.txt")
m = open("output.txt", "w")
capacity, quantity = map(int, f.readline().split())
weights = list(map(int, f.readline().split()))

weights.sort()
dp = []
for i in range(quantity + 1):
    dp.append([0]*(capacity + 1))

for i in range(1, quantity + 1):
    for j in range(1, capacity + 1):
        if weights[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + weights[i - 1])

print(dp)
m.write(str(dp[quantity][capacity]))

f.close()
m.close()
print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")