import time
import os, psutil


def knapsack(capacity, values, weights):
    items = []
    for i in range(len(values)):
        itemInfo = {
            'vpw': values[i] / weights[i],
            'weight': weights[i]
        }
        if len(items) == 0:
            items.append(itemInfo)
        else:
            k = 0
            while k < len(items) and items[k]['vpw'] > itemInfo['vpw']:
                k += 1
            items.insert(k, itemInfo)
    total = 0
    capacity_left = capacity
    for item in items:
        if capacity_left - item['weight'] >= 0:
            total += item['weight'] * item['vpw']
            capacity_left -= item['weight']
        elif capacity_left > 0:
            total += item['vpw'] * capacity_left
            capacity_left = 0
    return total


process = psutil.Process(os.getpid())
t_start = time.perf_counter()
f = open("input.txt")
m = open("output.txt", "w")
main_info = list(map(int, f.readline().split()))
capacity = main_info[1]
count = main_info[0]
values = []
weights = []
for i in range(count):
    info = list(map(int, f.readline().split()))
    values.append(info[0])
    weights.append(info[1])
m.write(str(knapsack(capacity, values, weights)))
f.close()
m.close()
print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")