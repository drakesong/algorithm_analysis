# CS 317 Algorithm Anaylsis Lab 2
# Drake Song
# Python 3.6

import numpy as np
import timeit
import os

os.system('cls')
time = []
ans = []

n = int(input("Enter a number greater than 2: "))
matrix = np.random.randint(-100, 100, size=(n-1, n)).tolist()

# print("\nInitial matrix:")
# print(np.matrix(matrix))

for a in range(5):
    tic = timeit.default_timer()
    for k in range(n-2):
        largest = 0
        row = 0
        for i in range(k, n-1):
            if np.absolute(matrix[i][k]) > largest:
                largest = np.absolute(matrix[i][k])
                row = i

        temp = matrix[k]
        matrix[k] = matrix[row]
        matrix[row] = temp

        # print("\nMatrix after swap:")
        # print(np.matrix(matrix))

        for i in range(k+1, n-1):
            ratio = matrix[i][k]/matrix[k][k]
            temp = [np.absolute(matrix[k][j]*ratio) for j in range(n)]
            if matrix[i][k] > 0:
                matrix[i] = [matrix[i][j] - temp[j] for j in range(n)]
            else:
                matrix[i] = [matrix[i][j] + temp[j] for j in range(n)]

        # print("\nMatrix after subtraction:")
        # print(np.matrix(matrix))

    toc = timeit.default_timer()
    time.append((toc-tic)*1000000)

print(sum(time)/5)
