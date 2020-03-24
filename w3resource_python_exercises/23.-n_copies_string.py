
# Get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2

user_string = str(input("Write your string: "))

def n_copies_str(my_str,n):
    if len(my_str) < 2:
       return my_str*n
    else:
       return (my_str[0] + my_str[1])*n

print(n_copies_str(user_string,2))






