import os
import time

limit=3
pass_num = 1  # pass number

tmp_list=[];    #temporary list variable
data={}


students=0
employees=0
unemployees=0




def ventry():
            global limit
            choice = [0, 1, 2, 3]
            os.system("cls")
            print("DATA SCIENCE SEMINAR\n")
            print('-' * 30)

            print('\t\t\tMENU')
            print('-' * 30)
            print("""
                    1.New Visitor
                    2.Visitor List
                    3.Categorywise Summary
                    0.Exit
                    """)

            item = input("Enter your code 0-3 :")

            if item == "":
                os.system("cls")
                ventry()




            item=int(item)
            if item not in choice:
                os.system("cls")
                ventry()


            if (item == 1):
                if limit==0:
                    print("HOUSE FULL")
                    print("\n")
                    input("Press any key to Continue...")

                a = newvisitor()
                limit-=1
                print(a)

                input("\nPress any key to Continue...")


            elif item == 2:
                print("TWO")
                vlist()

            elif item == 3:
                print("Three")
                summary()

            elif item == 0:
                exit()

            else:
                print(item)
                print("Enter a valid option")
                # continue



    # ==============screen1=================


def newvisitor():
    running = 1  # to control while loop execution only once
    global pass_num
    global tmp_list
    global data
    global students
    global employees
    global unemployees
    print("pass number=" + str(pass_num))
    while running:
        os.system('cls')
        print("Welcome to DSIT Seminar")

        participant_name = str(input("enter the Name of the participant:").lower())
        # tmp_list.append(participant_name)
        if (len((participant_name)) == 0):
            break
        place = str(input("enter the Place:").lower())
        if (len((place)) == 0):
            break
        category = str(input("enter the Category S/E/U").lower())
        if (len((category)) == 0):
            break
        print(category)
        if (category == "s"):
            category = "s"
            students += 1
        elif category == "e":
            category = "e"
            employees += 1

        elif category == "u":
            category = "u"
            unemployees += 1
        else:
            print("enter the correct values for category")  # alert if wrong value is entered
            input("Press any key to Continue...")
            break


  # =      # output ----------------------------
        os.system('cls')
        print("""                Data Science In Tamil
                         Anna Salai, Chennai
                        Seminar on Data Science

                         E N T R Y P A S S
                         """)
        print("Pass No  :", pass_num)

        print("Name     :", participant_name)

        print("Category :", category)

        print("""
        """)

        # -----------adding to dictionary

        data[pass_num] = [participant_name,category]
        # ------------------------------------
        pass_num = pass_num+1

        input("Press any key to Continue...")
        os.system('cls')
        running = 0


# ==============screen1=================


def vlist():
    global data
    print(data.items())
    input("Press any key to Continue...")

def summary():
    global data
    global students
    global employees
    global unemployees


    print('The number of students : ' + str(students))
    print('The number of Employees : ' + str(employees))
    print('The number of UnEmployees : ' + str(unemployees))

    input("Press any key to Continue...")



running = 1
while(running):
    ventry()