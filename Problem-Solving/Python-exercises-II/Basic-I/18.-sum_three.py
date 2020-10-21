
# Calculate the sum of three given numbers, if the values are equal then return three times of their sum

def three_sum(a,b,c):
    if a == b == c:
        my_sum3 = (a+b+c)*3
        return my_sum3
    else:
        my_sum = a + b + c
        return my_sum

print("The sum is", three_sum(3,3,3))









