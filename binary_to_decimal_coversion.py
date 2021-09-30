# Here we take a binary number and convert it to decimal
# Remember, Binary is a place value system with 2 symbols: 1 and 0. Each place value is a power of 2

import sys

user_binary = input('Please enter a binary number to convert to decimal? 1\'s and 0\'s only please!')
print(type(user_binary))

for i in user_binary:
	if i == '0' or i == '1':
		continue
	else:
		print(f'Sorry, {user_binary} is not a binary number. A binary number consistis only of 1\'s and 0\'s. Try again later after lunch....')
		sys.exit()

# Now let's get the len of the binary number and create an associated list for place values

place_values = []
binary_list = []
to_the_power = 0
for i in user_binary:
	place_values.append(2**to_the_power)
	to_the_power += 1
place_values.reverse()

for i in user_binary:
	binary_list.append(int(i))

print(binary_list)
print(place_values)

decimal_value = 0

for i in range(len(binary_list)):
	if binary_list[i] == 1:
		decimal_value += place_values[i]

print(f'The binary {user_binary} to decimal is {decimal_value}.')