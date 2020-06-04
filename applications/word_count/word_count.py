import re

def word_count(s):
    # create a dict to store the count for each word
    count = dict()

    # create a new string by converting all whitespace in the input string
    # to regular spaces and converting all text to lowercase
    string_with_spaces = re.sub(r'[^a-zA-Z0-9\' ]+', ' ', s).lower()

    # split the new string at each space into a list of individual words
    word_list = string_with_spaces.split(' ')

    # for each word in this list...
    for word in word_list:

        # if the word is an empty string, return to the beginning of the for loop
        if word == '':
            continue

        # if the word is already in our count dict, increment its counter by 1
        if word in count:
            count[word] += 1
        # otherwise, set that word's count to 1 in our count dict
        else:
            count[word] = 1

    # return the dict of words and their counts
    return count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))