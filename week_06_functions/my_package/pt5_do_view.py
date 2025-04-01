#doview.py

#Author: Faolán Hamilton
'''
students = []

#defining the function read_modules, but this has not been used in the below only add names.
def read_modules () :
    return []

    #current_student = a dictionary, to store the record title and the actual record, e.g. "name" : Mary
def do_add (students) :
    current_student = {}
    current_student ["name"] = input("Enter name : ")
    current_student ["modules"] = read_modules ()
# now we are appending the dict the user will create to the empty student list previously created
    students.append(current_student)

#test

do_add (students)

do_add (students)
'''

#defining the function read_modules, but this has not been used in the below only add names.
def display_modules (modules) :
    for module in modules:
        print (f"\t Module Name: {module['name']} \n \t Grade: {module['grade']}")


def do_view (students):
    for current_student in students:
        print (current_student ["name"])
        display_modules (current_student["modules"])

