
# Objective: Create the cow and bulls game

import random   # For randomness

# Turns a number into an array with every digit as an element
def num_array(user_input):
    return [int(i) for i in str(user_input)]

# Checks if the input is correct. It must be a 4 digits number
def if_mistake(user_input):

    while True:

        correct = 0

        if len(num_array(user_input)) != 4:
            print("Error.")
            print("You must write a 4 digits number!")
            user_input = int(input("Try again: "))

        for i in num_array(user_input):
            if isinstance(i,int) == False:
                print("Error.")
                print("You must write a 4 digits number!")
                user_input = int(input("Try again: "))
            else:
                correct += 1

        if correct == 4:
            return user_input

# Creating a main() function to prevent possible bugs if someone imports the file
def main():

    print("Welcome to the cow and bulls game!")

    random_num = random.randint(1000,9999)  # Between 1000 and 9999
    print("Random number:", random_num)

    tries = 1

    user_input = int(input("Write a number of 4 digits: "))

    if_mistake(user_input)

    # It will be asking for numbers until the user guesses the number
    while True:

        bull = 0
        cow = 0

        for i in range(4):
            if num_array(user_input)[i] in num_array(random_num):
                if num_array(user_input)[i] == num_array(random_num)[i]:    # Same position
                    cow += 1
                else:
                    bull += 1

        # Continue asking for a number until cow == 4
        if cow == 4:
            print("Congratulations! You won!")
            print("Number of tries:", tries)
            break
        else:
            print("Cows =", cow, "Bulls =", bull)
            tries += 1
            user_input = str(input("Try again: "))
            if_mistake(user_input)

if __name__ == "__main__":  # Main function
    main()