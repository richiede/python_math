# Here's a small program that accepts an input and checks if it is a prime number

user_number = int(input('Enter a number to check if it it prime: '))

is_prime = ''
for i in range(2, user_number):
    if user_number % i == 0:
        print(f'The number is not prime. It is divisible by {i}.')
        is_prime = 'n'
        break
    else:
        continue

if not is_prime == 'n':
    print('The number is prime!')
