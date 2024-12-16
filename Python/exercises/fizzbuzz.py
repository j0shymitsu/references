# If a number is divisible by 3, print FIZZ
# If a number is divisible by 5, print BUZZ
# if a number is divisible by both 3 and 5, print FIZZBUZZ
# Up to 100.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "FIZZBUZZ")
    elif i % 3 == 0:
        print(i, "FIZZ")
    elif i % 5 == 0:
        print(i, "BUZZ")
    else:
        print(i)
    