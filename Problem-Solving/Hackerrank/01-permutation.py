
# Complete the absolutePermutation function in the editor below. It should return an integer that represents the smallest lexicographically smallest permutation, or -1 if there is none.

# absolutePermutation has the following parameter(s):

#     n: the upper bound of natural numbers to consider, inclusive
#     k: the integer difference between each element and its index


def absolutePermutation(n, k):
    if k == 0:
        return [i for i in range(1,n+1)]
    if n%2 == 0 and n%(k*2) == 0:
        values_list = [i for i in range(1,n+1)]
        result_list = [0 for i in range(n)]
        x = 0
        while x<n/k:
            for i in range(k*x,k*x+k):
                result_list[i] = values_list[i+k]
            for i in range(k*x+k,k*x+2*k):
                result_list[i] = values_list[i-k]
            x += 2
        return result_list
    else:
        return [-1]

