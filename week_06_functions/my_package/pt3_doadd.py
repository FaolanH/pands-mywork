#doadd.py

#Author: Faolán Hamilton

# a. Read in the student’s name (that is straightforward)
# b. Read in the module names and grades (this is a bit more complicated 
# c. Test this function, it creates a student dict, we can print that out.
# d. We should add the student dict to list (pass this list in)
# e. Test this.

# This file is going to activate the choices we have been developing in the last few files, allowing student names and modules to be passed through 

#an empty list where the students records will be stored

#defining the function read_modules, but this has not been used in the below only add names.

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

    #current_student = a dictionary, to store the record title and the actual record, e.g. "name" : Mary
def do_add (students) :
    current_student = {}
    current_student ["name"] = input("Enter name : ")
    current_student ["modules"] = read_modules ()
# now we are appending the dict the user will create to the empty student list previously created
    students.append(current_student)

#test
'''
do_add (students)

do_add (students)
'''
#REMOVE THIS BEFORE PIECING EVERYTHING TOGETHER
