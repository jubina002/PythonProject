class BankAccount:
    def __init__(self, name, phone, balance = 0.0):
        self.name = name 
        self.phone = phone
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            print(f"Deposit Rs{amount: .2f} to {self.name}'s account")
        else:
            print("Invalid deposit amount")  
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs{amount: .2f} from {self.name}'s account")
        else:
            print("Invalid Withdraw amount or insufficient balance")

    def get_amount(self):
        return f"{self.name}'s current balance: Rs{self.balance: .2f}"
    
    
ram = BankAccount("Ram", +977-9832134)
ram.deposit(5000)
ram.withdraw(500)

print(ram.get_amount())