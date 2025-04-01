

#ptY_easier_written_menu.py

#Author: Faolán Hamilton

from my_package.pt3_doadd import do_add
from my_package.pt5_do_view import do_view

# ------------------MENU CHOICE-------------------
def menu_choice ():
    print("What would you like to do? ")
    print ("\t a) Add new student")
    print ("\t v) View students")
    print ("\t q) Quit")
    choice = input("Type one letter (a/v/q)")
    return choice

#----------------------DEFINING THE OPTIONS A, V, Q-----------------------------
    #the dict that maps a letter to function
choice_map = {
'a': do_add,
'v': do_view,
'q': lambda x: None # q is a valid choice
}

#-------------------------MAIN PROGRAM--------------------------------------
students = []
choice = menu_choice ()
while(choice != 'q'):
    if choice in choice_map:
        # run the function
        choice_map[choice] ( students)
    else: # use did not enter something valid
        print("\n\nplease select either a,v or q")
    
    choice=menu_choice ()

print ("Program terminated.")