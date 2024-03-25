class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls,obj):
        cls.hall_list.append(obj)


class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        super().__init__()
        self.seats = {}
        self.show_list = [("Jawan",11,"11.30"),("Raees",12,"02:30")]
        # self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
    
    def entry_show(self,movie_name,id, time):
        self.show_list.append(tuple((movie_name, id,  time)))
        self.seats[id] =  [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    def book_seats(self,id,seat_id):
        pass
    def view_show_list(self):
        print()
        if(len(self.show_list) > 0):
            for i in self.show_list:
                print(f"Movie Name: {i[0]} | ID: {i[1]} | Time: {i[2]}")
            print()
        else:
            print("No upcoming shows! Stay Tuned.")
    def view_available_seats(self,id):
        flag = False
        for i in self.show_list:
            if(i[1] == id):
                flag = True
                print("\n",self.seats[id],"\n********************\n")  # show the seat that are available for the show
        if(flag == False):
            print("-----------------\nKindly provide a valid id! \n-----------------")







# hall1 = Hall(5, 10, 1)
# hall1.entry_hall(hall1)

# # Initialize an object of Hall with rows, cols, and hall_no
# hall2 = Hall(3, 5, 2)

# # Call the entry_show() method of the first object of Hall
# hall1.entry_show("123", "Movie1", "14:00")

# # Call the entry_show() method of the second object of Hall
# hall2.entry_show("456", "Movie2", "16:00")



# # Print the hall_list attribute of the Star_Cinema object
# print(Star_Cinema.hall_list)

# # Print the show_list attribute of the first object of Hall
# print(Star_Cinema.hall_list[0].show_list)

# # Print the seats attribute of the first object of Hall
# print(Star_Cinema.hall_list[0].seats)



while(True):
    inp = int(input("1. View all shows today. \n2. View available seat. \n3. Book ticket. \n4. Exit \n\nEnter your option: "))
    hall1 = Hall(2,2,1)
    hall1.entry_show("Fighter",77,"12.01")
    if(inp == 1):
        hall1.view_show_list()
    elif(inp == 4):
        break
    elif(inp == 2):
        hall1.view_available_seats(77)