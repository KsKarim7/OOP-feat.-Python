class Account:
    def __init__(self,email,password):
        print("\nPlease Sign Up to your account:")
        self.__email = email
        self.__password = password

    def login(self,email,password):
        if(self.__email == email and self.__password == password ):
            print("Successfully logged in you account!")


    