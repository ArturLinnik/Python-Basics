
# Objective: asks the user how many Fibonnaci numbers to generate and then generates them.

def get_integer():
    return int(input("Fibonacci numbers to generate: "))

def fibonacci(num_iter):
    if num_iter == 0:
        fib_list = []
    elif num_iter == 1:
        fib_list = [1]
    elif num_iter == 2:
        fib_list = [1,1]
    else:
        i = 1
        fib_list = [1,1]
        while i < num_iter-1:
            fib_list.append(fib_list[i] + fib_list[i-1])    # Fibonacci sucession
            i += 1
    return fib_list

print(fibonacci(get_integer()))