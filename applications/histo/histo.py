import re
from bst import BSTNode

with open('robin.txt') as f:
    read_data = f.read()

# convert all whitespace in read_data to regular spaces
# and convert all text to lowercase
read_data = re.sub(r'[^a-zA-Z0-9\' ]+', ' ', read_data).lower()

# split the string of data into a list of individual words, and create a new dict
word_list = read_data.split(' ')
word_dict = dict()

# create a variable to store the length of the longest word in the data
longest_length = 0

# for each word in the list...
for word in word_list:

    # if the word is an empty string, return to the beginning of the for loop
    if word == '':
        continue

    # if the word is already in the dict, increment its counter by 1 at its 0-index
    # and add another '#' to its string at its 1-index
    if word in word_dict:
        word_dict[word][0] += 1
        word_dict[word][1] += '#'
    # otherwise, if not already in the dict, set the k/v for this entry to [1, '#']
    else:
        word_dict[word] = [1, '#']

        # if the current word is longer than the previously longest, update the variable
        if len(word) > longest_length:
            longest_length = len(word)

# increment the longest word's character count by 2 to account for the
# two spaces specified in the instructions before printing the hash marks
longest_length += 2

sorted_items_list = sorted(word_dict.items(), key = lambda e: e[1][0], reverse=True)
n = len(sorted_items_list)

for i in range(n-1):
    if int(sorted_items_list[i][1][0]) == int(sorted_items_list[i+1][1][0]) and str(sorted_items_list[i][0][0]) > str(sorted_items_list[i+1][0]):
        sorted_items_list[i], sorted_items_list[i+1] = sorted_items_list[i+1], sorted_items_list[i]

for item in sorted_items_list:
    print(f'{item[0]:{longest_length}}{item[1][1]}')
