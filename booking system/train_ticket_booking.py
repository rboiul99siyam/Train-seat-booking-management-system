class Train():
    def __init__(self,name,train_id,location,destination) -> None:
        self.name = name
        self.train_id = train_id
        self.location = location
        self.destination = destination
class Admin(Train):
    passenger = []
    train_list = []
    seats = {}

    def __init__(self,email):
        self.email = email
    
    def add_train(self,name,train_id,location,destination):
        new_train = Train(name,train_id,location,destination)
        self.train_list.append(new_train)
        print("Train Added successfully !!\n\n")

        seat = []
        for i in range(10):
            seat.append(["A",'A','A',"A",'A'])
            self.seats[train_id] = seat

    
    def show_avaliable_train(self):
        for train in self.train_list:
            print("---------------------------------------------------------------------------")
            print(f"name : {train.name} id : {train.train_id} location : {train.location} destination : {train.destination}")
            print("--------------------------------------------------------------------------")
    def show_available_seats(self,train_id):
        for i in self.seats[train_id]:
            for j in i:
                print(j,end=' ')
            print()
    def book_seats(self,train_id):
        row = int(input("Enter row : "))
        col = int(input("Enter column : "))
        if self.seats[train_id][row][col] == "X":
            print("This seat is already booked !!")
        else:
            self.seats[train_id][row][col] = "X"
            print("Booking Seats Successfully \n")
    

    def show_all_users(self):
        for user in self.passenger:
            print(user.name)


    
class User():
    def __init__(self,name,possword,email) -> None:
        self.name = name
        self.possword = possword
        self.email = email
        

admin = Admin("admin@gamil.com")

while True:
    user_type = input("admin / user ? ")
    if user_type == "user":
        print("\n-- 1.  Login now : ")
        print("\n-- 2.  Regester now : ")
        print("\n-- 3.  Exit now : ")

        ch = int(input("\n\n-----Choose your option(1,2,3):  "))
        if ch == 1:
            possword = int(input("----Enter Your Possword: "))
            email = input("---Enter Your email : ")
            flag = False
            for user in admin.passenger:
                if user.possword == possword and user.email == email:
                    flag = True
                    print("--------------------------------------------------\n")
                    print("Welcome,",user.name)
                    while True:
                        print("\n--------1. show avaiable train -----")
                        print("\n--------2. show available seats ------")
                        print("\n--------3. Book seats ---------")
                        print("\n--------4. Logout   ---------")
                        op = int(input("choice Your option (1,2,3) :"))
                        if op == 1:
                            admin.show_avaliable_train()
                        elif op == 2:
                            id = int(input("Train id "))
                            admin.show_available_seats(str(id))
                        elif op == 3:
                            id = int(input("Train id "))
                            admin.book_seats(str(id))

                        elif op == 4:
                            print("\n\tLogout Successfully !!!!")
                            break

                else:
                    print("\n\n----invalid possword \n\n")

                    

        elif ch == 2:
            name = input("---Enter your name : ")
            possword = int(input("----Enter your possword : "))
            email = input("----Enter your Email : ")

            new_user = User(name,possword,email)
            admin.passenger.append(new_user)
            print("\n\n Regester on Successfully !!!!!\n\n")


    elif user_type == "admin":
        poss = int(input("\n-----Enter Your possword : "))
        email = input("\n------Enter Your email : ")

        if poss == 12345 and email == "admin":
            print("\n\n---Admin login Successfully")
            while True:
                print("----1.   add Train ")
                print("----2.   show all user ")
                print("----3.   show the avaliable train ")
                print("----4.   logout  ")
                op = int(input("choice your option : "))
                if op == 1:
                    name = input("Enter your Train name : ")
                    id = input("Enter Your Train id number : ")
                    locanation = input("Enter your location : ")
                    destination  = input("Enter Your destination : ")
                    admin.add_train(name,id,locanation,destination)
                elif op == 2:
                    admin.show_all_users()
                elif op == 3:
                    admin.show_avaliable_train()
                elif op == 4:
                    print("Logout successfully !!!")
                    break
