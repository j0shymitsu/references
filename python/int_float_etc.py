x = float(input("Please enter value 1: "))
y = float(input("Please enter value 2: "))

z = x / y

print(f"{z:,}") # The comma inputs the commas on larger numbers.

print(f"{z:.2f}") # ".2f" on decimals specificies the number of places to round to.