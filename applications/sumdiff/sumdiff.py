"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = set(range(1, 10))
# q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# create three empty dicts to store our sums, differences & combinations 
sums = dict()
differences = dict()
combos = dict()

for n1 in q:
    # for each number in q, if it's not already in the combos dict,
    # run f() on the number & store the return value in the combos dict
    if n1 not in combos:
        combos[n1] = f(n1)

    for n2 in q:
        # for each additional number in q, if not already in the combos dict,
        # run f() on the number & store the return value in the combos dict
        if n2 not in combos:
            combos[n2] = f(n2)

        # calculate the current sum & difference of f(n1) & f(n2)
        curr_sum = combos[n1] + combos[n2]
        curr_diff = combos[n1] - combos[n2]

        # if the current sum is already in the sums dict,
        # append [n1, n2] to the list at its index position in the sums dict
        if curr_sum in sums:
            sums[curr_sum].append([n1, n2])
        else:
            # otherwise, store [n1, n2] in the empty slot
            sums[curr_sum] = [[n1, n2]]

        # if the current difference is already in the differences dict,
        # append [n1, n2] to its list at its index position in the differences dict
        if curr_diff in differences:
            differences[curr_diff].append([n1, n2])
        else:
            # otherwise, store [n1, n2] in the empty slot
            differences[curr_diff] = [[n1, n2]]

for value in sums:
    # for each value in the sums dict, if it's also in the differences dict,
    # iterate through the ranges of the sums then differences dicts to
    # print an answer string for each value in their ranges based on the instructions
    if value in differences:
        for i in range(len(sums[value])):
            for j in range(len(differences[value])):
                print(f'f({sums[value][i][0]}) + f({sums[value][i][1]}) = f({differences[value][j][0]}) - f({differences[value][j][1]})    {combos[sums[value][i][0]]} + {combos[sums[value][i][1]]} = {combos[differences[value][j][0]]} - {combos[differences[value][j][1]]}')

