
# Sum of three given integers. However, if two values are equal sum will be zero

def sumThreeEqZero(x,y,z):
    if x == y or y == z or x == z:
        return 0
    else:
        return x + y + z

print(sumThreeEqZero(1,2,3))














