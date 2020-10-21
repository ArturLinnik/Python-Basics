
# Given a matrix of N rows and M columns you can choose a row/column and change the state of all the elements (0 -> 1 1 -> 0). In the end you have to interpret each row as the binary representation of a number and return the maximum sum of all the N numbers.

import numpy

def flipSum(matrix, n, m):
    matrix = numpy.array(matrix)
    for i in range(n):
        if matrix[i][0] != 1:
            matrix[i] = 1 - matrix[i]
    for i in range(1,m):
        if matrix.sum(axis=0)[i] < m/2:
            matrix[:,i] = 1 - matrix[:,i]
            matrix[:,i] *= 2**(m-1-i)

    matrix[:,0] *= 2**(m-1)
    return matrix.sum()

input_matrix = [[0,1,1,1],[1,1,0,0],[0,1,1,1]]

print(flipSum(input_matrix,3,4))
