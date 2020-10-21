
# Get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference

user_input = int(input("Write your number: "))

    
diff = abs(17 - user_input)

if user_input > 17:

    double_diff = diff*2
    print(double_diff)

else:

    print(diff)








