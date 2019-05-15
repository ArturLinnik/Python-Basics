
import random

# Generate two random lists with a length between 0 and 10 and random integers between 1 and 9

random_list1 = list(random.sample(range(10),random.randint(1,9)))
random_list2 = list(random.sample(range(10),random.randint(1,9)))

final_list = []

# Create a list where numbers that are common between the two lists are saved

rep_list = [num for num in random_list1 if num in random_list2]

# Save in the "final_list" the numbers the numbers without repetition

for num in rep_list:
    if num not in final_list:
        final_list.append(num)

# Print the two lists to know what numbers are in every list

print(random_list1)
print(random_list2)
print(final_list)