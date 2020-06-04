# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

def crack_caesar(file):

    # stores the frequencies provided in the instructions
    provided_freqs = dict()
    # stores the count for each letter
    counts = dict()
    # stores the current frequency of letters
    current_freqs = dict()
    # stores the total amount of letters
    total = 0
    # create a string of all letters to iterate through
    a_z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # for each letter, set it's initial value to 0 in counts & current_freqs
    for letter in a_z:
        counts[letter] = 0
        current_freqs[letter] = 0

    # save all frequencies provided in the project's instructions
    provided_freqs['E'] = 11.53
    provided_freqs['T'] = 9.75
    provided_freqs['A'] = 8.46
    provided_freqs['O'] = 8.08
    provided_freqs['H'] = 7.71
    provided_freqs['N'] = 6.73
    provided_freqs['R'] = 6.29
    provided_freqs['I'] = 5.84
    provided_freqs['S'] = 5.56
    provided_freqs['D'] = 4.74
    provided_freqs['L'] = 3.92
    provided_freqs['W'] = 3.08
    provided_freqs['U'] = 2.59
    provided_freqs['G'] = 2.48
    provided_freqs['F'] = 2.42
    provided_freqs['B'] = 2.19
    provided_freqs['M'] = 2.18
    provided_freqs['Y'] = 2.02
    provided_freqs['C'] = 1.58
    provided_freqs['P'] = 1.08
    provided_freqs['K'] = 0.84
    provided_freqs['V'] = 0.59
    provided_freqs['Q'] = 0.17
    provided_freqs['J'] = 0.07
    provided_freqs['X'] = 0.07
    provided_freqs['Z'] = 0.03

    # open the provided file and store the encrypted data in a variable
    with open(file) as file:
        encrypted_data = file.read()
    
    # iterate through each character in the encrypted data and
    # increment its counters in counts and total if it already exists in counts
    for x in encrypted_data:
        if x in counts:
            counts[x] += 1
            total += 1

    # calculate the current frequency that each letter is used by dividing its
    # value in counts by the total number of letters, then store it in current_freqs
    for letter in a_z:
        current_freqs[letter] = counts[letter] / total

    # convert both frequency dicts to lists of tuples so we can sort them
    current_freqs = current_freqs.items()
    provided_freqs = provided_freqs.items()

    # sort both frequency lists based on each tuple's frequency value,
    # which is the second value in each tuple (1-index)
    provided_freqs = sorted(provided_freqs, key=lambda letter: letter[1])
    current_freqs = sorted(current_freqs, key=lambda letter: letter[1])

    # join each of the two sorted lists of tuples into strings
    # using the value at their 0-index (the letter only)
    encrypted_joined = ''.join([letter_data[0] for letter_data in current_freqs])
    decrypted_joined = ''.join([letter_data[0] for letter_data in provided_freqs])

    # create a mapping table using the maketrans() method to generate
    # a 1-to-1 mapping of each letter in the cipher to its translation
    mapping_table = encrypted_data.maketrans(encrypted_joined, decrypted_joined)

    # use the mapping table and translate() method to return a string
    # which will translate the cipher into readable English text
    ans = encrypted_data.translate(mapping_table)

    # return the decrypted string
    return ans


decrypted_cipher = crack_caesar('ciphertext.txt')

with open('decrypted.txt', 'w') as file:
    file.write(decrypted_cipher)