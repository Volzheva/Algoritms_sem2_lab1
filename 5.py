import time
import os, psutil
import math


def decision_dop(summa):
    '''Рассмотрим арифметичесую посоедовательность с шагом 1(начало - 1),
    Поселедний элемент - 1 + n , сумма = (((1+n) + 1) * n) / 2
    '''
    discr = 4 + 8 * summa
    count = math.floor((-2 + math.sqrt(discr))/2)
    print(count)
    ostatok = int(summa - ((count + 1) * count / 2))
    numbers = []
    for i in range(count + 1):
        numbers.append(1 + i)
    numbers[-1] += ostatok
    return numbers


def decision(summa):
    numbers = [1]
    while sum(numbers) <= summa:
        numbers.append(numbers[-1] + 1)

    numbers.pop()
    ostatok = int(summa - sum(numbers))
    numbers[-1] += ostatok
    return numbers


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("input.txt")
m = open("output.txt", "w")
summa = int(f.readline())
our_decision = decision(summa)
m.write(str(len(our_decision)) + "\n")
for i in range(len(our_decision)):
    m.write(str(our_decision[i]) + " ")
f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
