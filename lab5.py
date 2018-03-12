# CS 317 Algorithm Anaylsis Lab 5
# Drake Song
# Python 3.6

import numpy as np
from numpy import linalg as LA

def powerMethod(A, x0, x00, eig, tol0, tol1):
    tol = tol0
    err = 1
    iteration = 0
    maxCount = 150
    end = False
    while err > tol:
        iteration += 1
        # print("Iteration: " + str(iteration))
        x1 = A * x0
        norm = LA.norm(x1, np.inf)
        x1 = 1/norm * x1
        err = np.sqrt(np.dot((x1-x0).T, (x1-x0)))
        x0 = x1
        # print("Error: " + str(err.item(0)))
        # print("Eigenvector: ")
        # print(x0)
        # print("Eigenvalue: " + str(norm))
        # print()
        if iteration+1 > maxCount:
            print("Maximum Iterations exceeded")
            print()
            end = True
            break
    if  not end:
        print("Iteration: " + str(iteration))
        print("Tolerance: " + str(tol))
        print("Error: " + str(err.item(0)))
        print("Eigenvector: ")
        print(x0)
        print("Eigenvalue: " + str(norm))
        print()

        err = 1
        iteration = 0
        x0 = x00
        tol = tol1
        while err > tol:
            iteration += 1
            # print("Iteration: " + str(iteration))
            y = LA.inv(A - (-18 * np.identity(A.shape[0]))) * x0
            x1 = y/LA.norm(y)
            norm = x1.T * A * x1
            err = abs(eig - norm)
            x0 = x1
            # print("Error: " + str(err.item(0)))
            # print("Eigenvector: ")
            # print(x0)
            # print("Eigenvalue: " + str(norm))
            # print()
            if iteration+1 > maxCount:
                print("Maximum Iterations exceeded")
                print()
                end = True
                break
        if  not end:
            print("Iteration: " + str(iteration))
            print("Tolerance: " + str(tol))
            print("Error: " + str(err.item(0)))
            print("Eigenvector: ")
            print(x0)
            print("Eigenvalue: " + str(norm))
            print()

def problem(n):
    if n == 1:
        print("Problem 1")
        A = np.matrix([[9,1,2,3], [-3,12,1,-1], [0,2,20,5], [3,1,-1,-18]])
        x0 = np.matrix([1,1,1,1]).T
        x00 = np.matrix([[-10,-1,-2,0]]).T
        eig = LA.eig(A)[0].item(0).real
        tol0 = 0.005
        tol1 = 0.000000005
        powerMethod(A, x0, x00, eig, tol0, tol1)
        print(LA.eig(A))
    elif n == 2:
        print("Problem 2")
        A = np.matrix([[0,1,0,0,0], [1,0,1,0,0], [0,1,0,1,0], [0,0,1,0,1], [0,0,0,1,0]])
        x0 = np.matrix([1,1,1,1,1]).T
        x00 = np.matrix([-1,0,-1,0,0]).T
        eig = LA.eig(A)[0].item(2).real
        tol0 = 0.005
        tol1 = 0.005
        powerMethod(A, x0, x00, eig, tol0, tol1)
        print(LA.eig(A))
    elif n == 3:
        print("Problem 3")
        A = np.matrix([[100,99,0], [0,99,0], [0,99,98]])
        x0 = np.matrix([1,1,1]).T
        x00 = np.matrix([-1,0,-1]).T
        eig = LA.eig(A)[0].item(1).real
        tol0 = 0.005
        tol1 = 0.05
        powerMethod(A, x0, x00, eig, tol0, tol1)
        print(LA.eig(A))
    elif n == 4:
        print("Problem 4")
        A = np.matrix([[100,3,0], [0,99,0], [0,4,98]])
        x0 = np.matrix([1,1,1]).T
        x00 = np.matrix([-1,0,-1]).T
        eig = LA.eig(A)[0].item(2).real
        tol0 = 0.005
        tol1 = 0.05
        powerMethod(A, x0, x00, eig, tol0, tol1)
        print(LA.eig(A))
    elif n == 5:
        print("Problem 5")
        A = np.matrix([[8,3,0], [-2,7,0], [0,0,4]])
        x0 = np.matrix([0,0,10]).T
        x00 = np.matrix([-1,0,-1]).T
        eig = LA.eig(A)[0].item(0).real
        tol0 = 0.005
        tol1 = 0.05
        powerMethod(A, x0, x00, eig, tol0, tol1)
        print(LA.eig(A))
    elif n == 6:
        print("Problem 6")
        row = 5
        col = 5
        low = -50
        high = 50
        A = np.random.choice([x for x in range(low,high)],row*col)
        A.resize(row,col)
        print(A)
        x0 = np.matrix([1,1,1,1,1]).T
        x00 = np.matrix([-1,1,0,0,0]).T
        eig = LA.eig(A)[0].item(0).real
        tol0 = 0.005
        tol1 = 0.005
        powerMethod(A, x0, x00, eig, tol0, tol1)
        print(LA.eig(A))

def main():
    problem(1)
    problem(2)
    problem(3)
    problem(4)
    problem(5)
    problem(6)


main()
