# CONTINUE  
## A continue statement immediately halts the current iteration and jumps to the next one
numbers = [16, -4, 25, -9, 36, 0, 49]

for number in numbers:
    if number < 0:
        continue        # Skip negatives to avoid complex numbers

    print(f'The square root of {number} is {number ** 0.5}.')

# BREAK
## A break statement exits the loop entirely
for n in range(42):
    print(f'{n} * {n} = {n * n}')

    if n * n > 150:
        break