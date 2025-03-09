#student.py
#Author: Faolán Hamilton

student = {
    "student_name" : 'Mary', 
    "modules" : [
        {"course_name" : "Programming and Scripting", 
        "grade" : 55},
        {"course_name" : "Principles of Data Analytics", 
        "grade" : 62}
    ]
   }

print (f" Student: {student["student_name"]}")
for module in student["modules"]:
    print(f"\t {module["course_name"]} \t: {module["grade"]}")