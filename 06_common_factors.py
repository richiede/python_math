# Find common multiples
# Here you will enter n integers, a list of common multiples will be returned
# EXAMPLE:
# Enter a whole number to check common factors: 27
# Press "y" to enter another number or any other key to quit: 54
# [1, 3, 9, 27]

# initial the starting list
initial_list = [10050, 120, 5000]

# add values to starting list for checking common multiples
#another_num = 'y'
#while another_num == 'y':
#    initial_list.append(int(input('Enter a whole number to check common factors: ')))
#    another_num = input('Press "y" to enter another number or any other key to quit: ')

# sort list into order            
initial_list.sort()

# intiialise the common multiples list
common_multiples = []

# check each digit in the in the range 0 to the lowest integer to check if
# it is a factor. If the digit is a factor of all of them it is added to
# the common multiples list
for i in range(1, initial_list[0] +1):
    checker = ''
    for p in range(len(initial_list)):
        if initial_list[p] % i == 0:
            checker = 'y'
        else:
            checker = 'n'
            break
    if checker == 'y':
        common_multiples.append(i)
    else:
        continue

print(common_multiples)
