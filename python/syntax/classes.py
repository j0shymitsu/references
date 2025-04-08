


###################
### INHERITANCE ###
###################



# A class for employees:
class Employee():
    
    raise_amt = 1.10

    def __init__(self, first, last, job=None):
        self.first = first
        self.last = last
        self.pay = 65000
        self.email = f"{first.lower()}.{last.lower()}@webentry.co.uk"
        self.job = job
        print("Employee created.")

    def __str__(self):
        class_desc = "First name is: " + self.first + "\n"
        class_desc += "Last name is: " + self.last + "\n"   # += Appends the string; otherwise it would be overwritten.
        class_desc += "Employee pay is: " + str(self.pay) + "\n"
        class_desc += "First name is: " + self.email + "\n"
        if self.job == None:
            pass
        else:
            class_desc += "Their role is: " + str(self.job)

        return class_desc
    
    def change_last(self, last):
        self.last = last
        print("Last name is changed.")
        print()

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        print(f"{self.first}'s pay is raised to: {str(self.pay)}")  # int must be converted to string; although this isn't necessarily required in formatted (f) strings.

    def full_name(self):
        return f"{self.first} {self.last}"

# A subclass (inherited) for developers:    
class Developer(Employee):
    def __init__(self, first, last, prog_lang):
        super().__init__(first, last)   # Calls the method from parent class
        self.prog_lang = prog_lang
        print(f"Employee {self.full_name()} is a {prog_lang} developer.")

    def __str__(self):
        class_desc = super().__str__()
        class_desc += f"Programming language: {self.prog_lang}\n"
        return class_desc

josh = Employee("Josh", "Birch", "Programmer")
print(josh)
print()

josh.change_last("Abracadabra")
print(josh)
print()

josh.apply_raise()
print(josh)
print()

print(josh.full_name())
print()

dave = Developer("Dave", "Smith", "Python")
print(dave)

