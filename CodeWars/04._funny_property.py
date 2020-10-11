# Some numbers have funny properties. For example:

#     89 --> 8^1¹ + 9^2² = 89 * 1

#     695 --> 6^2² + 9^3³ + 5^4= 1390 = 695 * 2

#     46288 --> 4^3³ + 6^4+ 2^5 + 8^6 + 8^7 = 2360688 = 46288 * 51

# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

#     we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.

# In other words:

#     Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

# If it is the case we will return k, if not return -1.

# Note: n and p will always be given as strictly positive integers.

def dig_pow(n, p):
    sum_num = 0
    for i in str(n):
        sum_num += int(i)**p
        p += 1
    if sum_num%n == 0:
        k = sum_num/n
        return int(k)
    else:
        return -1

print(dig_pow(46288,3))

