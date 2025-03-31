#display_menu.py

#Author: Faolán Hamilton

# In part 2, we continue the menu options, but add in a lo'op to have a better definition appear - aka, now if the
# user inputs a, 'in adding' appears, v 'in viewing' appears and q they quit.
# the functions (which will be defined in other files) have also been called

def menu_choice ():
    print("What would you like to do? ")
    print ("\t a) Add new student")
    print ("\t v) View students")
    print ("\t q) Quit")
    choice = input("Type one letter (a/v/q)")
    return choice
def do_add ():
    print ("in adding")

def do_view ():
    print ("in viewing")

choice = menu_choice ()

while choice != "q":

    if choice == "a":
        do_add ()

    elif choice == "v":
        do_view ()

    elif choice != "q":
        print ("\n\n please select either a, v or q") 
    choice = menu_choice ()

print (choice)