
# Objective: Showing the divisors of a number using a for loop.

number = int(input("Write a number and I'll show you its divisors: "))

div_list = [num for num in range(1,number+1) if number%num == 0]

print(div_list)