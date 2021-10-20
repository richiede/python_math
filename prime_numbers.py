# Sieve of Eratosthenes
#STEP 1: Create a list of consecutive unsigned integers from 2 to chosen “n”: (2, 3, 4, 5, 6 ..., n).
#Here we use 2 - 100

user_num = int(input('Enter a number greater than 2 that you want to find all the prime numbers up till: '))
my_list = list(range(2, user_num))

#STEP 2: 2 will be the starting prime number assigned “p”

p = my_list[0]
n = my_list[-1]

#STEP 3: Enumerate through the list in multiples of p through to n (or the largest multiple of p before n). #Cross them off the list
#STEP 4: Find the smallest value in the list greater than p. This is the next prime number and mark this as p.
#STEP 5: Repeat steps 3 and 4 till there are no further numbers left greater than p after step 4.

prime_list = []
while len(my_list) > 0:
    try:
        no_check = []
        for i in my_list:
            if i % p == 0:
                #print(i)
                no_check.append(i)
                my_list.remove(i)
        p = my_list[0]        
        prime_list.append(no_check[0])
        #some_input = input()
    except IndexError:
        continue
prime_list.append(no_check[0])
print(prime_list)

#STEP 6: Algorithm complete.
