#read_modules.py

#Author: Faolán Hamilton

#in this file, we are now defining the modules

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

    return modules

print (module)