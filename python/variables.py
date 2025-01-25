age = input("Enter your age: ")

print(type(age))
age = int(age)
print(type(age))

birth_year = 2024 - age
print(f"You were born in {birth_year} or {birth_year - 1}")

### 

player_name = "String"

player_alive = True

player_health = 1000
print(player_health)
player_health = 900
print(player_health)

armor_multiplier = 2
armored_health = player_health * armor_multiplier
print(armored_health)

variables_names_need_to_be_in_snack_case = True

###

x = float(input("Please enter value 1: "))
y = float(input("Please enter value 2: "))

z = x / y

print(f"{z:,}") # The comma inputs the commas on larger numbers.

print(f"{z:.2f}") # ".2f" on decimals specificies the number of places to round to.
