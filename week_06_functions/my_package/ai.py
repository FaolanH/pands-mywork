# Author: Faolán Hamilton

import pt3_doadd as do_add, pt5_do_view as do_view

# ------------------MENU CHOICE-------------------
def menu_choice():
    print("What would you like to do?")
    print("\t a) Add new student")
    print("\t v) View students")
    print("\t q) Quit")
    choice = input("Type one letter (a/v/q): ")
    return choice

# the dict that maps a letter to function
choice_map = {
    'a': do_add.do_add,
    'v': do_view.do_view,
    'q': lambda x: None  # q is a valid choice
}

# main program
students = []
choice = menu_choice()
while choice != 'q':
    if choice in choice_map:
        # run the function
        choice_map
    else:  # user did not enter something valid
        print("\n\nPlease select either a, v, or q")
    
    choice = menu_choice()

print(do_view.do_view)
