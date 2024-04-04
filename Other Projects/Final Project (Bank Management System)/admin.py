from bank import Bank
from user import User

class Admin(Bank):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)

    

    def delete_user(self,user):
        for i in Bank.users:
            if(i.name == user):
                Bank.users.remove(i)
                print("User removed. ✅")

    def user_accounts(self):
        print('Current users:', ', '.join(user.name for user in User.users))

    def show_balance(self):
        print(Bank.balance)
    
    def show_loans(self):
        print(Bank.loans)
    
    def can_take_loan(self,bool):
        Bank.if_loan = bool

