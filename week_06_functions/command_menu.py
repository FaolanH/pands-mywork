#student_management.py

#Author: Faolán Hamilton

def menu_choice ():
    print("What would you like to do? ")
    print ("\t a) Add new student")
    print ("\t v) View students")
    print ("\t q) Quit")
    choice = input("Type one letter (a/v/q)")
    if choice == "a":
        print ("Add new student")

    elif choice == "v":
        print ("View students")

    elif choice == "q":
        print ("Quit") 

    else:
        print ("Please input either a/v/q")         
    return choice

choice = menu_choice ()

print (choice)