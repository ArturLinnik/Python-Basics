
# Objective: See if a word is a palindrome or not.

word = str(input("Write a word: "))   # User's input

if word == word[::-1]:  # Reverse word
    print("It's a palindrome")
else:
    print("It isn't a palindrome")

