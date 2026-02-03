# Build a BankAccount Class
class BankAccount:
    def __init__(self, owner_name, starting_balance):
        self.owner_name = owner_name
        self.starting_balance = starting_balance
        self.current_balance = 0
        self.current_balance += starting_balance
    
    def deposit(self, amount):
        self.current_balance += amount
        return self.current_balance
        
    def withdraw(self, amount):
        if amount > self.current_balance:
            pass
        else:
            self.current_balance -= amount
        return self.current_balance
    
    def get_balance(self):
        return self.current_balance