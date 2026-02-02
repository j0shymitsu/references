


###################################
### OBJECT ORIENTED PROGRAMMING ###
###################################



# EMPLOYEE LIST #

# Class for employee:
class Employee():   # Defines a class; class name always has a capital letter.
    
    company = "University of Chester"   # Class variable.

    def __init__(self, name, role, pay):    # Initialiser method.
        self.name = name
        self.role = role    # Instance variables.
        self.pay = pay
        print("\nNew employee created:")    # !! Not best practice to have output in init method in larger scale applications.

    def __str__(self):  # Returns information string.
        resultstr = f"Name: {self.name.title()}  |  Role: {self.role.upper()}  |  Pay: £{self.pay:,}"
        return resultstr
    
    def hello(self):
        print(f"Hello, my name is {self.name}\n")

    def payrise(self, increment):
        self.pay = round(self.pay * increment, 2)
        if increment > 1.1:
            increment = 1.1
        print(f"Payrise added for {self.name}. Their salary is now {self.pay}")

# Adding employees to the class:
bob = Employee("Bob", "Manager", 50000)
print(bob)

josh = Employee("josh", "CEO", 250000)
print(josh)

# Updating an instance:
bob.pay = 60000
print(f"\nSalary updated: Bob's salary is now {bob.pay}.")
print(bob)
print()

# Calling methods within a class:
bob.hello()
print()

bob.payrise(1.05)
print(bob.name, bob.company)



# STUDENT LIST #

# Class for students:
class Student():
    
    institution = "University of Chester"

    def __init__(self, name, course, current_year):
        self.name = name
        self.course = course
        self.current_year = current_year
        print("\nNew student created:")

    def __str__(self):
        resultstr = f"Summary: {self.summary.title()}  |  Academic year: {self.current_year}"
        print()
        return resultstr
    
    @property
    def summary(self):
        return self.name + ' - ' + self.course
    
    def change_year(self, new_year):
        self.current_year = (0 + new_year)
        if new_year > 6:
            print(f"Current year updated for {self.name}, this student has now graduated.")
        else:
            print(f"Curerent year updated for {self.name}, they are now in year {self.current_year}")

dave = Student("dave", "computing", 2)
print(dave)

