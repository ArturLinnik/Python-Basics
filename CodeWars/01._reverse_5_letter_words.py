# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    splitted_sentence = sentence.split()

    for i in range(len(splitted_sentence)):
        if len(splitted_sentence[i]) >= 5:
            word_to_reverse = splitted_sentence[i]
            reversed_word = word_to_reverse[::-1]
            splitted_sentence[i] = reversed_word

    return ' '.join(splitted_sentence)

my_sentence = "This is a sentence"

print(spin_words(my_sentence))

