age = input("Enter your age: ")

print(type(age))
age = int(age)
print(type(age))

birth_year = 2024 - age
print(f"You were born in {birth_year} or {birth_year - 1}")