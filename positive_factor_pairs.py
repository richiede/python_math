# Here we will find the positive factor pairs of a positive integer
# Example: Enter a number to find it's positive factor pairs: 12
# Output: [[1, 12], [2, 6], [3, 4]]

# initialise the variable assuming a positive int will be entered
num = int(input('Enter a number to find it\'s positive factor pairs: '))

# create the list of numbers we will be working with
num_list = [x for x in range(1, num +1)]

# create a list of lists with pairs
pair_list = []

# Here we loop through the list
for i in num_list:
    # set the initial variable
    first_pair = i
    for y in num_list:
        # the calculation
        if first_pair * y == num:
            second_pair = y
            # set the pair
            pair = [first_pair, second_pair]
            # sort the pair to ensure no duplicates
            pair.sort()
            if pair not in pair_list:
                pair_list.append(pair)

print(pair_list)
