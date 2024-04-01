class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls,obj):
        cls.hall_list.append(obj)


class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        super().__init__()
        self.__seats = {}
        # self.show_list = [("Jawan",11,"11.30"),("Raees",12,"02:30")]
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
    
    def entry_show(self,movie_name,id, time):
        self.__show_list.append(tuple((movie_name, id,  time)))
        self.__seats[id] =  [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    
    def book_seats(self,id,seat_id):
        if(id not in self.__seats):
            print("-----------------\nKindly provide a valid id! \n-----------------")
        for n in seat_id:
            if(n[0] > self.rows or n[1] > self.cols):
                print("Invalid Seat Number\n")
            else:
                if(self.__seats[id][n[0]][n[1]] != 0):
                    print("Your preferred seat is already booked! Kindly select other available seats.")
                else:
                    self.__seats[id][n[0]][n[1]] = 1

    def view_show_list(self):
        print()
        if(len(self.__show_list) > 0):
            for i in self.__show_list:
                print(f"Movie Name: {i[0]} | ID: {i[1]} | Time: {i[2]}")
            print()
        else:
            print("No upcoming shows! Stay Tuned.")
    def view_available_seats(self,id):
        flag = False
        for i in self.__show_list:
            if(i[1] == id):
                print("Updated seats matrix for Hall no. ",self.hall_no)
                flag = True
                print("\n",self.__seats[id],"\n********************\n")  # show the seat that are available for the show
        if(flag == False):
            print("-----------------\nKindly provide a valid id! \n-----------------")



hall1 = Hall(3,3,1)
hall1.entry_show("Fighter",77,"12.01")

while(True):
    inp = int(input("1. View all shows today. \n2. View available seat. \n3. Book ticket. \n4. Exit \n\nEnter your option: "))
    if(inp == 1):
        hall1.view_show_list()
    elif(inp == 4):
        break
    elif(inp == 2):
        n = int(input("Enter show id: "))
        hall1.view_available_seats(n)
    elif(inp == 3):
        hall1.book_seats(77,[(4,1),(0,0)])