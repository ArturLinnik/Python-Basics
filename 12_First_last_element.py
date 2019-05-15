
# Objective: takes a list and makes a new list with the first and the last element.

import random

def rand_list():
    return list(random.sample(range(10),random.randint(1,9)))

def first_last(in_list):
    first_last_list = [in_list[0], in_list[len(in_list)-1]]
    return first_last_list

list_a = rand_list()

print(list_a)

print(first_last(list_a))