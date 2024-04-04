from bank import Bank
import random  

class User(Bank):
    def __init__(self,name,email,address,typ) -> None:
        super().__init__(name,email,address)
        self.typ = typ
        self.acc_no = str(name[:2]) + str(random.randint(7,77))
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
        self.transactions["Deposit"] += amount
    
    def withdraw(self,amount):
        if(self.can_withdraw):
            if(amount > self.balance):
                print("Withdrawal amount exceeded") 
            else:
                self.balance -= amount
                self.transactions["Deposit"] -= amount
                self.transactions["Withdraw"] += amount
        else:
            print("You are Bankrupt ❌")

    def __repr__(self):
        return f'Your current account balance is ${self.balance}'

    def transaction_history(self):
        for k,v in self.transactions.items():
            print(f"***{k}: ${v}***")

    def take_loan(self,amount):
        if(self.loan_limit <= 0 or Bank.if_loan == False):
            if(self.loan_limit <= 0):
                print('Your loan limit exceeded.')
            else:
                print("Sorry, Bank is current not eligible for giving loans.")
        else:
            self.loan_limit -= 1
            self.balance += amount
            self.transactions['Loan'] += amount
            Bank.balance -= amount
            Bank.loans += amount
    def transfer_money(self,amount,user):
        if(amount <= self.balance):
            for i in Bank.users:
                if(i.name == user):
                    i.balance += amount
                    self.balance -= amount
                    print("Money transferred successfully!!")
                    
            # if(to_user.name in Bank.users):
            #     to_user.balance += amount
            #     self.balance -= amount
                else:
                    print("Account does not exist")
        else:
            print("Insufficient balance!")
        
