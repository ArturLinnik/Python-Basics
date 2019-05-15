
list_a = []
final_list = []

# Creating a list like: [1, 4, 9, 16, ...]

for num in range(1,11):
    list_a.append(num**2)

for num in list_a:
    if num%2 == 0:  # Even numbers
        final_list.append(num)

print(final_list)

