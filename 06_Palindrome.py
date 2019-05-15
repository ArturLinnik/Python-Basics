
word = str(input("Write a string: "))   # User's input

if word == word[::-1]:  # Reverse word
    print("It's a palindrome")
else:
    print("It isn't a palindrome")

