from account import Account
import random  

class User(Account):
    users = []
    def __init__(self,name,email,address,typ) -> None:
        super().__init__(name,email,address)
        User.users.append(name)
        self.typ = typ
        self.acc_no = name[:2] + random.randint(7,77)
        self.loan_limit = 2
        self.transactions = {
            "Deposit": 0,
            "Withdraw": 0,
            "Loan": 0
        }
        self.balance = 0
        self.can_withdraw = True
    
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if(self.can_withdraw):
            if(amount > self.balance):
                print("Withdrawal amount exceeded") 
            else:
                self.balance -= amount
        else:
            print("You are Bankrupt ❌")

    def __str__(self):
        return f'You current account balance is ${self.balance}'

    def transaction_history(self):
        for k,v in self.transactions.items():
            print(f"***{k}: {v}***")

    def take_loan(self,amount):
        if(self.loan_limit <= 0):
            print('Your loan limit exceeded.')
        else:
            self.loan_limit -= 1
            self.balance += amount
            self.transactions['Loan'] += amount
    
    def transfer_money(self,amount,to_user):
        if(amount < self.balance):
            if(to_user.name in User.users):
                to_user.balance += amount
                self.balance -= amount
            else:
                print("Account does not exist")
        else:
            print("Insufficient balance!")
        
