import os

No_of_Participants = 0
No_of_Students = 0
No_of_Employees = 0
No_of_Un_Employees = 0
categorye_check = True
name_check = True
place_check = True
user_input_check = True
total_no_lsit = []
name_list = []
place_list = []
category_list = []


os.system("clear")
max_users_allowed = int(
    input("What is the maximum number of users allowed ?  "))
os.system('clear')


def manu_board():
    """This function is to bring the GUI for the main screen """

    print("DATA SCIENCE SEMINAR".rjust(33), "-" *
          50, "MANU".rjust(25), "-"*50, sep="\n")
    print("1. New Visitor", "2. Visitor List",
          "3. Categorywise Summary", "0. Exit", sep="\n")
    print("-"*50)
    return " "


def is_number(user_input):
    """This function will check the user input whether between 0 to 3 and not a numeric value"""

    if not user_input.isnumeric() or int(user_input) >= 4 or int(user_input) < 0:
        os.system("clear")
        print("please enter a valid number..!".upper(), end="\n"*4)
        return False
    else:
        return True


def add_vistor(user_input):
    """This function will add visitors to the system by pressing 1 and also it will check the inputs 
    are valid or not. Once the user input the value it will be added to the list to store the data. finally it will bring the result"""

    global No_of_Students
    global No_of_Participants
    global No_of_Students
    global No_of_Employees
    global No_of_Un_Employees

    print("-" * 50, "New Visitor Entry".rjust(32), "-"*50, sep="\n")
    name_check = True
    while name_check:
        name = input("Name of Participant                        :")
        if name.isalpha():
            name_check = False
            name_list.append(name.title())
        else:
            print("Name can't be empty or non Alphabet")
            continue

    place_check = True
    while place_check:
        place = str(input("Place                                      :"))
        if place.isalpha():
            place_check = False
            place_list.append(place.title())
        else:
            print("Place can't be leave empty or non Alphabet..!! ")
            continue

    category_check = True
    while category_check:
        category = str(
            input("Category (S)tudent/(E)mployee/(U)nEmployee :").lower())
        if category == "s":
            No_of_Students += 1
            category_check = False
            category = "Student"
            category_list.append(category.title())
        elif category == "e":
            No_of_Employees += 1
            category_check = False
            category = "Employee"
            category_list.append(category.title())
        elif category == "u":
            No_of_Un_Employees += 1
            category_check = False
            category = "Unemployee"
            category_list.append(category.title())
        else:
            print("Error..!! Please provide valid input..!!")
            continue

        No_of_Participants += 1
        total_no_lsit.append(No_of_Participants)

        os.system("clear")
        print("Data Science In Tamil".center(50), "Chennai".center(50), " ",
              "DATA SCIENCE SEMINAR".center(48), "E N T R Y  P A S S".center(48), sep="\n")
        print("-"*50)
        print(f"Pass No      : {No_of_Participants}")
        print(f"Name         : {name.upper()}")
        print(f"Place        : {place.title()}")
        print(f"Category     : {category.title()}")
        print("-"*50)
        print("\n"*20)
        any_key = input("press a key to continoue..")
        return os.system("clear")


def visitor_list(user_input):
    """This function will show the current visitors, who are already added to the system.
     The information will be loop through from the overall list"""

    print("DATA SCIENCE SEMINAR".center(63), ("-"*20).center(63),
          "Participant List".center(63), "-"*70, sep="\n")
    print("Sl.No.".ljust(10, " "), "Name of Participant".ljust(
        10, " "), "Place".rjust(12, " "), "Category".rjust(20, " "))
    print("-"*70)

    over_all_list = []
    over_all_list.insert(0, total_no_lsit)
    over_all_list.insert(1, name_list)
    over_all_list.insert(2, place_list)
    over_all_list.insert(3, category_list)

    for row in range(len(over_all_list[0])):
        for col in range(len(over_all_list)):
            print(str(over_all_list[col][row]).ljust(18), end=" ")
        print()

    print("-"*70)
    print("\n"*30)
    any_key = input("press a key to continoue..")
    os.system("clear")
    return " "


def categorywise_summary(user_input):
    """This function will print the count based on the category"""

    os.system("clear")
    print("Data Science In Tamil".center(50), "Chennai".center(50), " ",
          "DATA SCIENCE SEMINAR".center(48), "Summary".center(48), sep="\n")
    print("-"*50)
    print(f"No of Participan      : {No_of_Participants}")
    print(f"No of Students        : {No_of_Students}")
    print(f"No of Employees       : {No_of_Employees}")
    print(f"No of Un-Employees    : {No_of_Un_Employees}")
    print("-"*50)
    print("\n"*30)
    any_key = input("press a key to continoue..")
    os.system("clear")
    return " "


def housefull():
    """This function will check whether the participants reached the maximum loud"""
    if No_of_Participants < max_users_allowed:
        return True
    else:
        os.system("clear")
        print("HUOSE FULL")
        print("\n"*20)
        any_key = input("press a key to continoue..")
        return os.system("clear")


os.system("clear")
while True:
    print(manu_board())

    user_input = input("Enter your Code 0 to 3 :")
    if not is_number(user_input):
        continue

    if int(user_input) == 0:
        os.system("clear")
        print("Thank you for using our software - DIST Team")
        break

    if int(user_input) == 1 and housefull():
        os.system("clear")
        add_vistor(user_input)

    if int(user_input) == 2:
        os.system("clear")
        visitor_list(user_input)

    if int(user_input) == 3:
        os.system("clear")
        categorywise_summary(user_input)

