def no_dups(s):
    # create a dict to store our words
    word_dict = dict()
    # split the input string into a list of words
    word_list = s.split(' ')

    # for each word in the list...
    for word in word_list:

        # if the current word is in the dict, return to the beginning of the for loop
        if word in word_dict:
            continue
        # otherwise, add the current word to the dict
        else:
            word_dict[word] = 1

    # return a string which joins all of the words in the word dict
    return ' '.join(word_dict)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))