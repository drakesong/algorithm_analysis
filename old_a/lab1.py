# Python 3.6
# CS 317 Algorithm Analysis
# Lab 1
# Drake Song

import time

def primelist1(n):
    print("2 is prime")
    for j in range(3, n+1):
        isPrime = True
        for i in range(2, j):
            if j%i == 0:
                isPrime = False
        if isPrime:
            print("{} is prime".format(j))


def primelist2(n):
    print("2 is prime")
    for j in range(3, n+1):
        isPrime = True
        for i in range(2, int(j**(0.5))+1):
            if j%i == 0:
                isPrime = False
        if isPrime:
            print("{} is prime".format(j))


def primelist3(n):
    print("2 is prime")
    for j in range(3, n+1):
        isPrime = True
        for i in range(2, int(j**(0.5))+1):
            if j%i == 0:
                isPrime = False
                break
        if isPrime:
            print("{} is prime".format(j))


def primelist4(n):
    primeList = [2]
    for j in range(3, n+1):
        isPrime = True
        for i in range(2, int(j**(0.5))+1):
            if j%i == 0:
                isPrime = False
                break
        if isPrime:
            primeList.append(j)
    print(primeList)


a = int(input("Enter a number: "))
while a < 2:
    a = int(input("Please enter an integer greater than 1: "))

print("\nPrimeList1")
tic1 = time.time()
primelist1(a)
toc1 = time.time()

print("\nPrimeList2")
tic2 = time.time()
primelist2(a)
toc2 = time.time()

print("\nPrimeList3")
tic3 = time.time()
primelist3(a)
toc3 = time.time()

print("\nPrimeList4")
tic4 = time.time()
primelist4(a)
toc4 = time.time()

print("")
print("Time1: {}ms".format(round(1000*(toc1-tic1), 10)))
print("Time2: {}ms".format(round(1000*(toc2-tic2), 10)))
print("Time3: {}ms".format(round(1000*(toc3-tic3), 10)))
print("Time3: {}ms".format(round(1000*(toc4-tic4), 10)))
