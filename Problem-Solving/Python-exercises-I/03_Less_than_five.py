
# Objective: Prints all the numbers less than five in a list.

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print("This program will show all the numbers which are less than 5")

i = 0

while(i<len(list)):
    if (list[i]<5):
        print(list[i])
    i+=1

