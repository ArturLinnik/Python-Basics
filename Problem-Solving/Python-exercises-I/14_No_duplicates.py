
# Objective: Write a function that takes a list and makes a list without duplicates

import random

def nodup_list(user_list):
    return list(set(user_list))

def nodup_list_loop(user_list):
    new_list = []
    for num in user_list:
        if num not in new_list:
            new_list.append(num)
    return sorted(new_list) 

random_list = [random.choice(range(10)) for x in range(10)] # Create a random list with duplicates

print(random_list)

print(nodup_list(random_list))
print(nodup_list_loop(random_list))
