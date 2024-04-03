from user import User
from bank import Bank
from admin import Admin

def main():
    # user1 = User("Khalz",'kskarim9@gmail.com','9/1 kishan lane','current')
    # user2 = User("Khaled",'karim@gmail.com','9/1 kishan lane','current')
    # user3 = User("Nahid",'nahid@gmail.com','2 no.Nagad','saving')
    # user4 = User("Nahid2",'nahid2@gmail.com','2 no.Nagad2','saving')
    # admin = Admin("Mr.admin",'admin@hudai.com','brac-bank')
    
    # print("---------------User Interactions--------------- \n")
    # user1.deposit(70000)
    # user1.withdraw(17000)
    # user1.withdraw(700000)
    # print(user1)
    # user1.transaction_history()
    # user1.take_loan(7000)
    # user1.take_loan(75000)
    # user1.take_loan(700)
    # user1.transfer_money(70,user2)
    # user1.transfer_money(700000000,'Nahid (Nagad)')
    # print(user1)

    # print("\n---------------Admin Interactions--------------- \n")
    # admin.delete_user("Nahid2")
    # admin.user_accounts()
    # admin.show_balance()
    # admin.show_loans()
    # admin.can_take_loan(False)


    # user3.take_loan(100000000000000000000000000000000000000000000000)


    while(True):
        n = int(input("-> Press 1 to create an User account. \n-> Press 2 to create an Admin account. \n"))
        if(n == 1):
            print("Kindly fill the follow form to create your account. \n")
            name = input("Your name: ")
            email = input("Your email: ")
            address = input("Your permanent address: ")
            accTyp = input("Account type: ")
            user1 = User(name,email,address,accTyp)

            print("\nYour bank account has been created successfully! \n")
            print("Select the following options: \n")
            
            while(True):
                m = int(input("1. Deposit money. \n2. Withdraw money. \n3. My current balance. \n4. Previous Transactions. \n5. Transfer money. \n6. Take loan. \n7. Back to previous page.\nInput box: "))

                if(m == 1):
                    amount = int(input("Input your amount: "))
                    user1.deposit(amount)
                elif(m == 2):
                    amount = int(input("Input your amount: "))
                    user1.withdraw(amount)
                elif(m == 3):
                    print(user1)
                elif(m == 4):
                    user1.transaction_history()
                elif(m == 5):
                    a = int(input("How much? "))
                    i = input("To whom you want to transfer your money?")
                    user1.transfer_money(a,i)
                elif(m == 6):
                    l = int(input("Amount: "))
                    user1.take_loan(l)
                else:
                    break
            
            continue

        elif(n == 2):
            print("Kindly fill the follow form to create your account. \n")
            name = input("Your name: ")
            email = input("Your email: ")
            address = input("Your permanent address: ")
            admin = Admin(name,email,address)
            print("\nYour bank account has been created successfully! \n")
            print("Select the following options: \n")
            
            while(True):
                m = int(input("1. Delete account. \n2. See all users. \n3. Bank balance. \n4. Money on loan. \n5. Switch loan feature. \n. 6.Back to previous page. \nInput box: "))

                if(m == 1):
                    inp = input("User name? ")
                    admin.delete_user("inp")
                elif(m == 2):
                    admin.user_accounts()
                elif(m == 3):
                    admin.show_balance()
                elif(m == 4):
                    admin.show_loans()
                elif(m == 5):
                    inp = input("1. Type 'Yes' to turn on. \n2.Type 'No' to turn off.")
                    inp.upper()
                    if(inp == "YES"):
                        admin.can_take_loan(True)
                    else:
                        admin.can_take_loan(False)
                else:
                    break
            
            continue
        else:
            break




if __name__ == '__main__':
    main()