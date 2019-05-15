
# Objective: Write a function that takes a list and returns if the number is in the list or not.

import random

# Creates a list with random elements with the length of the list as the parameter.
def random_list(num_range, len_list):
    return [random.randint(1,num_range) for i in range(len_list)]

# Sorts the list in ascendent order. We can use the sorted(list) function too.
def sort_list(messy_list):
    i = 0
    while i < len(messy_list):
        n = i + 1
        while n < len(messy_list):
            if messy_list[i] > messy_list[n]:
                cambio = messy_list[i]
                messy_list[i] = messy_list[n]
                messy_list[n] = cambio 
            n += 1
        i += 1
    return messy_list

# Returns if the user's number is in the list or not.
def search_number(user_list, user_num):
    if user_num in user_list:
        return "Your number is in the list."
    else:
        return "Your number is not in the list."

# Asks the user for a number until the user inputs an int number.
def int_input(input_text):
    while True:
        try:
            user_int = int(input(input_text))
            return user_int
        except Exception as msg:
            print(msg)

# Main function
def main():

    user_range = int_input("Write in what range do you want your random numbers to be: ")

    user_len = int_input("Write the length of the list that you want: ")

    my_list = sort_list(random_list(user_range, user_len))
    print(my_list)  # Optional. To know what is in the list.

    user_num = int_input("Write the number you want to search for: ")

    print(search_number(my_list, user_num))
    
if __name__ == "__main__":
    main()


