
# Objective: Make a function that takes a string and returns that string with the words in backward order

def backw_string(user_string):
    word_list = user_string.split() # Convert every word in an element of a list
    return ' '.join(word_list[::-1])    # Joins every element in a string in reverse order

input_string = input("Write a string: ")
print(backw_string(input_string))