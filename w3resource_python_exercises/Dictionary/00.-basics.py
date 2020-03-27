
# A dictionary is a list of key-values separated by commas and ":"

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

# Get the value of the "model" key

x = thisdict["model"]
print (x)

y = thisdict.get("model")
print(y)

# Change values of an item referring to its key

thisdict["year"] = 2020
print (thisdict["year"])

# Loop through a dictionary using  a for loop

# Print all the key names

for i in thisdict:
    print(i)

# Print all the values

for i in thisdict:
    print(thisdict[i])

for i in thisdict.values():
    print(i)

# Print keys and values

for i,n in thisdict.items():
    print(i,n)

# Check if key exists

if "model" in thisdict:
    print(True)

# Dictionary length

print(len(thisdict))

# Add a new item

thisdict["color"] = "red"
print(thisdict)

# Remove items

thisdict.pop("model")
print(thisdict)

del thisdict["brand"]
print(thisdict)

del thisdict    # Deletes all the dictionary



thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Remove the last added item

thisdict.popitem()
print(thisdict)

# Empty the dictionary

thisdict.clear()
print(thisdict)



thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


# Copy a dictionary

first_copy = thisdict.copy()
print(thisdict)
print(first_copy)

second_copy = dict(thisdict)
print(thisdict)
print(second_copy)

 # Nested dictionaries (dictionaries that contains dictionaries)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 

# Make a new dictionary with dict()

thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)









