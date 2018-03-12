# Python 2.7

def primetest1(n):
    isPrime = True
    if n < 2:
        print "Error"
    elif n == 2:
        print isPrime
    else:
        for i in xrange(2, n):
            if n % i == 0:
                isPrime = False
        print isPrime


def primetest2(n):
    isPrime = True
    if n < 2:
        print "Error"
    elif n == 2:
        print isPrime
    else:
        for i in xrange(2, int(n**0.5)+1):
            if n % i == 0:
                isPrime = False
        print isPrime


def primetest3(n):
    isPrime = True
    if n < 2:
        print "Error"
    elif n == 2:
        print isPrime
    else:
        for i in xrange(2, int(n**0.5)+1):
            if n% i == 0:
                isPrime = False
                break
        print isPrime


def primelist1():
    n = int(raw_input("Please enter a number: "))




n = int(raw_input("Please enter a number: "))
print "\nPrime Test 1"
primetest1(n)
print "\nPrime Test 2"
primetest2(n)
print "\nPrime Test 3"
primetest3(n)
