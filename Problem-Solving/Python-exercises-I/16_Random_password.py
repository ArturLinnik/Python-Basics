 
# Objective: Make a random password

import random

# Creating lists of every type of elements

alph_list = [chr(character) for character in range(97,123)]
alphList = [chr(character) for character in range(65,91)]

num_list = [num for num in range(10)]

symbol_list = [chr(symbol) for symbol in range(33,48)]

# Making a two-dimensional list where are contained the four lists

twodim_list = []

twodim_list.append(alph_list)
twodim_list.append(num_list)
twodim_list.append(alphList)
twodim_list.append(symbol_list)

# Asking the user for the strength of their password

while True:

    user_input = str(input("How strong do you want your password? Type 'low', 'medium', 'hard' or 'ultra hard': "))

    if user_input == "low":
        user_num = 0
        break

    elif user_input == "medium":
        user_num = 1
        break

    elif user_input == "hard":
        user_num = 2
        break

    elif user_input == "ultra hard":
        user_num = 3
        break

# Choosing 20 random elements from every list

password = []

for elements in range(20):  # Our password will have 20 characters

    random_num = random.randint(0,user_num) # In function of the user_num the password will take
                                            # elements from the first to the fourth list
    if random_num == 0:
        password.append(str(twodim_list[random_num][random.randint(0,123-97-1)]))
    elif random_num == 1:
        password.append(str(twodim_list[random_num][random.randint(0,10-1)]))
    elif random_num == 2:
        password.append(str(twodim_list[random_num][random.randint(0,91-65-1)]))
    else:
        password.append(str(twodim_list[random_num][random.randint(0,48-33-1)]))

print(''.join(password))    
