from user import User
from bank import Bank
from admin import Admin

def main():
    user1 = User("Khalz",'kskarim9@gmail.com','9/1 kishan lane','current')
    user2 = User("Khaled",'karim@gmail.com','9/1 kishan lane','current')
    user3 = User("Nahid",'nahid@gmail.com','2 no.Nagad','saving')
    user4 = User("Nahid2",'nahid2@gmail.com','2 no.Nagad2','saving')
    admin = Admin("Mr.admin",'admin@hudai.com','brac-bank')
    
    print("---------------User Interactions--------------- \n")
    user1.deposit(70000)
    user1.withdraw(17000)
    user1.withdraw(700000)
    print(user1)
    user1.transaction_history()
    user1.take_loan(7000)
    user1.take_loan(75000)
    user1.take_loan(700)
    user1.transfer_money(70,user2)
    user1.transfer_money(700000000,'Nahid (Nagad)')
    print(user1)

    print("\n---------------Admin Interactions--------------- \n")
    admin.delete_user("Nahid2")
    admin.user_accounts()
    admin.show_balance()
    admin.show_loans()
    admin.can_take_loan(False)


    user3.take_loan(100000000000000000000000000000000000000000000000)





if __name__ == '__main__':
    main()