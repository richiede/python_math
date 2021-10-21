# This code takes a number, a guess of the square root, then calculates the actual square root - or close to it
# find the square root of a number
x = 45796

# Start with a guess g
g = 2

# if g * g is close enough to x, stop and say g is the answer
# otherwise make a new guess and by averaging g and x/g 
# repeat till close or complete

while g * g != x:
    g = (g + x / g) / 2
    print(f'new guess : {g}')

print(f'The square root of {x} is {g}!')
