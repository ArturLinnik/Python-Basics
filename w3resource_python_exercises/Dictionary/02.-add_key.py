
# Add a key to a dictionary

sample_dictionary = {0: 10, 1: 20}

def addKey(user_key, user_value):
    sample_dictionary[user_key] = user_value

addKey(2,30)
print(sample_dictionary)

# Another way is:

def addKey2(user_key, user_value):
    sample_dictionary.update({user_key:user_value})

addKey2(2,30)
print(sample_dictionary)















