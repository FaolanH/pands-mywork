#ptX_display_menu_tied_together.py

#Author: Faolán Hamilton

# In part 2, we continue the menu options, but add in a lo'op to have a better definition appear - aka, now if the
# user inputs a, 'in adding' appears, v 'in viewing' appears and q they quit.
# the functions (which will be defined in other files) have also been called

# ------------------MENU CHOICE-------------------
def menu_choice ():
    print("What would you like to do? ")
    print ("\t a) Add new student")
    print ("\t v) View students")
    print ("\t q) Quit")
    choice = input("Type one letter (a/v/q)").strip()
    return choice

#-------------------------ADD STUDENTS-------------------------
    #current_student = a dictionary, to store the record title and the actual record, e.g. "name" : Mary

def do_add (students) :
    current_student = {}
    current_student ["name"] = input("Enter name : ")
    current_student ["modules"] = read_modules ()
# now we are appending the dict the user will create to the empty student list previously created
    students.append(current_student)

#-------------------------ADD MODULES/GRADE--------------------------
# no error handling done - must remember anything within a function cannot be called outside of function

def read_modules () :
    modules = []
    module_name = input ("\t Enter the first module name (blank to quit): ").strip() # .strip() is used to remove any unneccesary spaces 

#because we have used .strip(), even is someone puts spaces in the module name this loop will still work
    while module_name != "":
        module = {}
        module ["name"] = module_name
        module ["grade"] = int(input ("\t\t Enter grade: "))
        modules.append(module)
        #read in next module name
        module_name = input("\t Enter next module name (blank to quit): ").strip()
     #important to keep in line within function   
    return modules

#-----------------------VIEWING--------------------------
#defining the function read_modules, but this has not been used in the below only add names.
def display_modules (modules) :
    for module in modules:
        print (f"\t Module Name: {module['name']} \n \t Grade: {module['grade']}")


def do_view (students):
    for current_student in students:
        print (current_student ["name"])
        display_modules (current_student["modules"])

#------------------------MAIN PROGRAM---------------------

students = []
choice = menu_choice ()

while choice != "q":

    if choice == "a":
        do_add (students)

    elif choice == "v":
        do_view (students)

    elif choice != "q":
        print ("\n\n please select either a, v or q") 
    choice = menu_choice ()