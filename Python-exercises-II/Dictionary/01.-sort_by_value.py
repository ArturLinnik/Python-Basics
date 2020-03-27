
import operator

# Sort (ascending and descending) a dictionary by value

example_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

dict_sorted = sorted(example_dict.items(), key = operator.itemgetter(1)) # Ascending
print(dict_sorted)


dict_sorted = dict(sorted(example_dict.items(), key = operator.itemgetter(1), reverse=True)) # Descending 
print(dict_sorted)





