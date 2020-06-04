import random

# Read in all the words in one go
with open('input.txt') as f:
    read_data = f.read()

# TODO: analyze which words can follow other words

word_list = read_data.split()
word_dict = dict()
start_words = []
n = len(word_list)

# traverse each word in the word_list
for i in range(n):

    # break the loop after the last word
    if i == n - 1:
        break

    # if the current word from word_list already exists in the dict
    # append the next word from word_list to the existing word in the current slot
    if word_list[i] in word_dict:
        word_dict[word_list[i]].append(word_list[i + 1])
    # otherwise, if the current word is not already in the dict
    # store the next word from word_list at the current slot in the dict
    else:
        word_dict[word_list[i]] = [word_list[i + 1]]

        # if the first letter of the word at the current index of word_list is a
        # (") symbol or an uppercase letter, append this word to the start_words list
        if word_list[i][0] == '"' or word_list[i][0].isupper():
            start_words.append(word_list[i])


# TODO: construct 5 random sentences

for _ in range(5):
    # set a pointer to check if we've reached the end
    over = False
    # choose a random word from the start_words list
    current = random.choice(start_words)
    # create an empty ans string which will be used to build the answer
    ans = ''
    # while over == False...

    while not over:
        # update the answer string by adding the random starting word and a space
        ans += current + ' '
        # choose a random word from the index of the current word in the dict
        current = random.choice(word_dict[current])
        # create a pointer set to the last character in the current word
        last_char = current[len(current) - 1]

        # if the last character is a . or ? or ! or "
        if last_char == '.' or last_char == '?' or last_char == '!' or last_char == '"':
            # create a pointer set to the second-to-last character in the current word
            previous_char = current[len(current) - 2]

            # if the last character in the word is a quotation mark (")
            # and the character before it is a . or ? or !
            # return to the beginning of the for loop
            if last_char == '"' and not (previous_char == '.' or previous_char == '?' or previous_char == '!' or previous_char == '"'):
                continue

            # update the answer string by adding the current word
            ans += current

            # print the answer string and set over to True
            print(ans)
            over = True
