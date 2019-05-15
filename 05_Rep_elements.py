
import random 

# Create 2 random lists

# Objective: take two lists and make a list that contains the elements in common without repetition.

list_a = list(random.sample(range(10),random.randint(1,9)))
list_b = list(random.sample(range(10),random.randint(1,9)))

final_list = []     # The result list

# Comparing the 2 lists

for num in list_a:
    if num in list_b:
        if num not in final_list:
            final_list.append(num)

print("First list: ", (list_a))
print("Second list: ", (list_b))

print("Result list: ", (final_list))

# The same objective but in a function and with sets

def rep_elements(user_list1, user_list2):
    norep_list = [x for x in user_list1 for y in user_list2 if x == y]
    return list(set(norep_list))

print(rep_elements(list_a, list_b))
