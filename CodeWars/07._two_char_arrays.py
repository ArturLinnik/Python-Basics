# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):
    str_array = []
    i = 0
    n = 2
    while i < len(s):
        str_array.append(s[i:n])
        i += 2
        n += 2
    if len(s)%2 == 0:
        return str_array
    else:
        str_array[-1] = s[-1]+"_"
        return str_array

##################

def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]

##################

import re

def solution(s):
    return re.findall(".{2}", s + "_")

##################

print(solution("Thiss"))
