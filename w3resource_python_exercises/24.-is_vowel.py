
# Test whether a passed letter is a vowel or not

def isVowel(chr):
    if chr == 'a' or chr == 'e' or chr == 'i' or chr == 'o' or chr == 'u':
        return True
    else:
        return False

print(isVowel('a'))


# Another way is:

def is_vowel(chr):
    all_vowels = "aeiou"
    return chr in all_vowels
        
print(isVowel('a'))







