# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

# Examples :

# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

def iq_test(numbers):
    numbers_split = numbers.split()
    numbers_split = list(map(int,numbers_split))
    n = 0
    for i in numbers_split:
        if i%2 == 0:
            n += 1
    if n>1:
        for i in numbers_split:
            if i%2 != 0:
                return numbers_split.index(i)+1
    else:
        for i in numbers_split:
            if i%2 == 0:
                return numbers_split.index(i)+1

def iq_test(numbers):
    numbers = [int(i)%2 for i in numbers.split()]
    if numbers.count(0)>1:
        return numbers.index(1)+1
    else:
        return numbers.index(0)+1


my_numbers = "10 9 10 6 8"
print(iq_test(my_numbers))
