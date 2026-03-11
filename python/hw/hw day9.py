class Account():
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __add__(self, other):
        return self._balance + other._balance

class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance *  0.05
    
class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02
    
savings = SavingsAccount("Ravi", 10000)
current = CurrentAccount("Anjali", 15000)

print("Account Details:\n")

print(f"Name: {savings._name}")
print(f"Balance: ₹{savings._balance}")
print(f"Interest: ₹{savings.calculate_interest()}\n")

print(f"Name: {current._name}")
print(f"Balance: ₹{current._balance}")
print(f"Interest: ₹{current.calculate_interest()}\n")

total_balance = savings + current
print(f"Total Balance (Savings + Current): ₹{total_balance}")
    