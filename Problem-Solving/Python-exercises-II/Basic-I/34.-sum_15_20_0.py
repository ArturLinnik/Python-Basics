
# Sum of two given integers. However, if the sum is between 15 to 20 it will return 20

def sumIf15To20ThenZero(x,y):
    sum = x + y
    if sum in range(15,20):
        return 20
    else:
        return sum

print(sumIf15To20ThenZero(12,6))















