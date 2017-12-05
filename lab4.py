# CS 317 Algorithm Anaylsis Lab 4
# Drake Song
# Python 3.6

import numpy as np

# Determine the functions according to the problem number
def f(p, x, y):
    if p == 1:
        return np.power(x,4) - 6 * np.power(x,2) + 8
    elif p == 2:
        return np.power(x,4) - 6 * np.power(x,2) + 9
    elif p == 3:
        return np.power(x,3) - 6 * np.power(x,2) + 9
    elif p == 4:
        return np.power(x,4) + 3 * np.power(x,2) + 2
    elif p == 5.1:
        return np.power(x,2) + np.power(y,2) - 4
    elif p == 5.2:
        return 3 * y - np.power(x,4)

# First derivative of the functions above
def fprime(p, x):
    if p == 1:
        return 4 * np.power(x,3) - 12 * x
    elif p == 2:
        return 4 * np.power(x,3) - 12 * x
    elif p == 3:
        return 3 * np.power(x,2) - 12 * x
    elif p == 4:
        return 4 * np.power(x,3) + 6 * x

# Newton's Method
def newton(p, x, y):
    return x - f(p,x,y)/fprime(p,x)

def problem1():
    print("Problem 1")

    # Boolean to determine if the root has been found (accurate to 15 deicmals places)
    different = True

    # Intial x_0 value
    n = 4

    # Run Newton's Method until convergence
    while different:
        a = newton(1,n,0)
        print('{0:.15f}'.format(a))
        if n == a:
            different = False
        else:
            n = a
    print("")

def problem2():
    print("Problem 2")
    different = True
    n = 4
    while different:
        a = newton(2,n,0)
        print('{0:.15f}'.format(a))
        if n == a:
            different = False
        else:
            n = a
    print("")

def problem3():
    print("Problem 3")
    print("Root 1")
    different = True
    n = 0 + 1j
    while different:
        a = newton(3,n,0)
        print('{0:.15f}'.format(a))
        if n == a:
            different = False
        else:
            n = a
    print("")

    print("Root 2")
    different = True
    n = -1 - 1j
    while different:
        a = newton(3,n,0)
        print('{0:.15f}'.format(a))
        if n == a:
            different = False
        else:
            n = a
    print("")

    print("Root 3")
    different = True
    k = 0
    n = 5 + 0j
    while different:
        a = newton(3,n,0)
        print('{0:.15f}'.format(a))
        k += 1
        if n == a or k == 20:
            different = False
        else:
            n = a
    print("")

def problem4():
    print("Problem 4")
    print("Root 1")
    different = True
    n = 0 + 4j
    while different:
        a = newton(4,n,0)
        print('{0:.15f}'.format(a))
        if n == a:
            different = False
        else:
            n = a
    print("")

    print("Root 2")
    different = True
    n = 0 - 4j
    while different:
        a = newton(4,n,0)
        print('{0:.15f}'.format(a))
        if n == a:
            different = False
        else:
            n = a
    print("")

    print("Root 3")
    different = True
    n = 2 + 0.5j
    while different:
        a = newton(4,n,0)
        print('{0:.15f}'.format(a))
        if n == a:
            different = False
        else:
            n = a
    print("")

    print("Root 4")
    different = True
    n = 2 - 0.5j
    while different:
        a = newton(4,n,0)
        print('{0:.15f}'.format(a))
        if n == a:
            different = False
        else:
            n = a
    print("")

# Jacobian Inverse Matrix for using Newton's Method on a system of 2 functions
def jacobianInverse(x, y):
    mat = np.matrix([[3, -2*y], [4 * np.power(x,3), 2*x]])
    det = 6*x + 8 * np.power(x,3) * y
    return (1 / det) * mat

def problem5(x,y):
    different = True
    while different:
        a = np.matrix([[x], [y]])
        b = jacobianInverse(x,y)
        c = np.matrix([[f(5.1,x,y)], [f(5.2,x,y)]])
        d = a - b * c
        x_1 = d.item(0)
        y_1 = d.item(1)
        print('[[ {0:.15f}]'.format(x_1))
        print(' [ {0:.15f}]]'.format(y_1))
        print()
        if x == x_1 and y == y_1:
            different = False
        else:
            x = x_1
            y = y_1


problem1()
problem2()
problem3()
problem4()
problem5(2,10)
print()
print()
problem5(-2,10)
