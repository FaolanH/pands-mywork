#student_userinput.py
#Author: Faolán Hamilton

modules = []

student_name = str(input("What is the student's name?: "))
module = str(input("What modules are they studying? (when you have finished entering them all, please press 0): "))

#ensures 0 = quit
while module != 0:
    modules.append(module)

    # next number 
    module = str(input("Please enter another module they study (press 0 to quit): "))

for value in modules:
    print (value)

print (modules)