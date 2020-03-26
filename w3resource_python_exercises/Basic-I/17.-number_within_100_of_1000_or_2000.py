
# Test whether a number is within 100 of 1000 or 2000

user_input = int(input("Write your number: "))

if (abs(1000 - user_input) <= 100 or abs(2000 - user_input) <= 100):
    print(True)

else:
    print(False)









