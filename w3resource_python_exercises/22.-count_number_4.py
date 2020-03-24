
# Count the number 4 in a given list

example_list = [1,2,3,4,5,6,4,3,4,2,1]

def number_of_4(my_list):

    counter = 0

    for i in my_list:
        if my_list[i] == 4:
            counter += 1

    return counter

print("The number of '4' is", number_of_4(example_list))











