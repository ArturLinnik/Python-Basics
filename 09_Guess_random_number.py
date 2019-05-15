
# Objective: Guess a random generated number.

import random

num_of_attempts = 0
user_num = 0

rand_num = random.randint(1,9)

print("I have generated a random number between 1 and 9.\nTry to guess it.")

while user_num != rand_num:
    user_num = int(input("Write your number: "))
    if user_num < rand_num:
        print("Too low. Try a bit higher.")
        num_of_attempts += 1
    elif user_num > rand_num:
        print("Too high. Try a bir lower.")
        num_of_attempts += 1
    else:
        print("Congratulations! You have guessed the number.")

print("You have made", num_of_attempts, "attempts.")