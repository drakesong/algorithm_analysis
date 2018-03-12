# CS 317 Algorithm Anaylsis Lab 2
# Drake Song
# Python 3.6

import numpy as np
import timeit
import os
import pdb

def clear():
    os.system('cls')

def addInt1():
    return 23 + 38

def addInt2():
    return 7261852 + 4917528

def multInt1():
    return 23 * 28

def multInt2():
    return 7261852 * 4917528

def divInt1():
    return 23 / 38

def divInt2():
    return 7261852 / 4917528

def addDoub1():
    return 23.3 + 38.1

def addDoub2():
    return 7261852.6 + 4917528.9

def multDoub1():
    return 23.3 * 38.1

def multDoub2():
    return 7261852.6 * 4917528.9

def divDoub1():
    return 23.3 / 38.1

def divDoub2():
    return 7261852.6 / 4917528.9

def sine():
    return np.sin(1.23)

def pwr():
    return np.power(3.13, 2.78)

def printStuff():
    for i in range(2):
        print(i)

def runFunction(n, x):
    time = []
    minimum = 0
    q1 = 0
    q3 = 0
    maximum = 0

    for i in range(n):
        for j in range(21):
            tic = timeit.default_timer()
            x()
            toc = timeit.default_timer()
            time.append((toc-tic)*1000000000)
        sorted_time = sorted(time)
        minimum += sorted_time[0]
        q1 += sorted_time[5]
        q3 += sorted_time[15]
        maximum += sorted_time[20]

    minimum /= n
    q1 /= n
    q3 /= n
    maximum /= n

    selected_time = [minimum, q1, q3, maximum]
    print(selected_time)

def runPrintStuff(n):
    time = []
    minimum = 0
    q1 = 0
    q3 = 0
    maximum = 0

    for i in range(n):
        for j in range(21):
            tic = timeit.default_timer()
            printStuff()
            toc = timeit.default_timer()
            time.append((toc-tic)*1000000000)

        sorted_time = sorted(time)
        minimum += sorted_time[0]
        q1 += sorted_time[5]
        q3 += sorted_time[15]
        maximum += sorted_time[20]

    clear()
    minimum /= n
    q1 /= n
    q3 /= n
    maximum /= n

    selected_time = [minimum, q1, q3, maximum]

    runFunction(n, addInt1)
    runFunction(n, addInt2)
    runFunction(n, multInt1)
    runFunction(n, multInt2)
    runFunction(n, divInt1)
    runFunction(n, divInt2)
    runFunction(n, addDoub1)
    runFunction(n, addDoub2)
    runFunction(n, multDoub1)
    runFunction(n, multDoub2)
    runFunction(n, divDoub1)
    runFunction(n, divDoub2)
    runFunction(n, sine)
    runFunction(n, pwr)

    print(selected_time)

n = int(input("Please enter a positive integer: "))
runPrintStuff(n)
