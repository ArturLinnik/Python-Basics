
# Get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged

user_string = str(input("Write your string: "))

user_array = user_string.split(' ')

if user_array[0] != "Is":
    user_array.insert(0,"Is")
    new_string = ' '.join(user_array)
    print(new_string)
else:
    print(user_string)
    











