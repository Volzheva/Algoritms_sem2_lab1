import time
import os, psutil
import math


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("input.txt")
m = open("output.txt", "w")
s = f.readline()
n = len(s)
dp = []
pos = []
for i in range(n):
    dp.append([0] * n)
    pos.append([0] * n)

for i in range(n):
    for j in range(n):
        if i == j:
            dp[i][j] = 1
for right in range(n):
    for left in range(right, -1, -1):
        if left == right:
            dp[left][right] = 1
        else:
            _min = math.inf
            mink = -1
            b1 = s[left] == '(' and s[right] == ')'
            b2 = s[left] == '[' and s[right] == ']'
            b3 = s[left] == '{' and s[right] == '}'
            if b1 or b2 or b3:
                _min = dp[left + 1][right - 1]
            for k in range(left, right):
                if _min > dp[left][k] + dp[k + 1][right]:
                    _min = dp[left][k] + dp[k + 1][right]
                    mink = k
            dp[left][right] = _min
            pos[left][right] = mink

print(dp)
print(pos)


def rec(l, r):
    temp = r - l + 1
    if dp[l][r] == temp:
        return
    if pos[l][r] == -1:
        m.write(s[l])
        rec(l + 1, r - 1)
        m.write(s[r])
        return
    rec(l, pos[l][r])
    rec(pos[l][r] + 1, r)


rec(0, n - 1)

f.close()
m.close()
print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
