
number = int(input("Write a number and I'll show you the divisor: "))

n = 0
i = 1
list_a = []

while (i<=number):
    if (number%i == 0):
        list_a.insert(n,i)
        n+=1
    i+=1
    
print(list_a)








