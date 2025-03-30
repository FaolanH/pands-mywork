#student_management.py

#Author: Faolán Hamilton

#This is part one of the student management system. In this file, we are setting the parameters for the program:
#we want to outline the options available to the user in the menu: add new student, view students or quit. 

def menu_choice ():
    print("What would you like to do? ")
    print ("\t a) Add new student")
    print ("\t v) View students")
    print ("\t q) Quit")
    choice = input("Type one letter (a/v/q)")
       
    return choice

choice = menu_choice ()

print (choice)