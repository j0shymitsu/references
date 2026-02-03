### COFFEE SHOP EXAMPLE ###



name = input("Please enter your full name: ")
print()

p1 = name.find(" ")
forename = name[:p1]
p2 = name.find(" ", p1+1)

# Checking if there is a middle name
if p2 != -1:
    middleName = name[p1+1:p2]
    p3 = name.find(" ", p2+1)
    if p3 != -1:
        surname = name[p2+1:p3]
    else:
        surname = name[p2+1:]
else:
    middleName = "N/A"
    surname = name[p1+1:]

print("Forename:", forename)
print("Middle name:", middleName)
print("Surname:", surname)
print()

icedCoffee = input("Are you ordering iced coffee? > ").lower()
if icedCoffee in ["y", "yes"]:
    icedCoffee = input("Please enter the number of iced coffees being purchased: ")
    print()

    icedCoffee = int(icedCoffee)
    total = icedCoffee * 2.95
    VAT = 0
    profit = icedCoffee * 1.95

    print("Total cost: £{:0.2f}".format(round(total, 2)))
    print("Total VAT paid: £{:0.2f}".format(round(VAT, 2)))
    print("Total profit to coffee shop: £{:0.2f}".format(round(profit, 2)))

else:
    coffee = input("Please enter the number of coffees being purchased: ")
    print()

    coffee = int(coffee)
    total = coffee * 2.95
    VAT = total - (total / 1.2)
    profit = coffee * 1.95

    print("Total cost: £{:0.2f}".format(round(total, 2)))
    print("Total VAT paid: £{:0.2f}".format(round(VAT, 2)))
    print("Total profit to coffee shop: £{:0.2f}".format(round(profit, 2)))
