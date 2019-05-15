
# Objective: Know if a number is prime or not.

def get_integer(text = "Write a number: "):
    return int(input(text))

user_num = get_integer()

def check_prime(x):
    check_var = 0
    for num in range(1,x+1):
        if x%num == 0:
            check_var += 1
    if check_var > 2:
        return print(x, "is not a prime number.")
    else:
        return print(x, "is a prime number.")

check_prime(user_num)