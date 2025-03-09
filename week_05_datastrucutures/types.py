#working with types
#Author: Faolán Hamilton

a_number_of_questions = 6
b_average_age = 34.7
c_debug_mode = True
d_name = "Faolán"
e_ages = []
f_months = ('Jan', 'Feb', 'March')
g_books = {}
h_random = [12, 'Hamilton', False, {}]
i_someone = dict(firstname = "Faolán")

j_me = {
    "firstname" : "Faolán", 
    "teaching" : [{
        "course_name" : "programming", 
        "semester": 1
    },{
        "course_name" : "data representation", 
        "semester": 2
    }
    ]
    }

guesses = []

#a_number_of_questions
while True:
    types = input(f"What type is a_number_of_questions {a_number_of_questions}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(a_number_of_questions).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")

#b_average_age
while True:
    types = input(f"What type is b_average_age {b_average_age}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(b_average_age).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")

#c_debug_mode
while True:
    types = input(f"What type is c_debug_mode {c_debug_mode}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(c_debug_mode).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")


#d_name
while True:
    types = input(f"What type is d_name {d_name}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(d_name).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")

#e_ages
while True:
    types = input(f"What type is e_ages {e_ages}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(e_ages).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")

#f_months
while True:
    types = input(f"What type is f_months {f_months}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(f_months).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")

#f_months_01
while True:
    types = input(f"What type is f_months {f_months [0]}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(f_months [0]).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")        

#g_books
while True:
    types = input(f"What type is g_books {g_books}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(g_books).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")


#h_random
while True:
    types = input(f"What type is h_random {h_random}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(h_random).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")

#h_random_2
while True:
    types = input(f"What type is h_random {h_random [2]}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(h_random [2]).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")

#i_someone
while True:
    types = input(f"What type is i_someone {i_someone}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(i_someone).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")


#i_someone_firstname
while True:
    types = input(f"What type is i_someone {i_someone ["firstname"]}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(i_someone ["firstname"]).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")

#j_me
while True:
    types = input(f"What type is j_me {j_me}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(j_me).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")

#j_me
while True:
    types = input(f"What type is j_me {j_me ["teaching"]}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(j_me ["teaching"]).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")

#j_me["teaching"][0]["semester"] 
while True:
    types = input(f"What type is j_me {j_me ["teaching"][0]["semester"] }?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(j_me ["teaching"][0]["semester"] ).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")

#j_me["teaching"][0]["coursename"]  
while True:
    types = input(f"What type is j_me {j_me["teaching"][0]}?: ")
    guesses.append(types)  # Record the user's input

    if types.lower() == type(j_me["teaching"][0]).__name__:
        print("Correct!")
        break
    else:
        print("False, try again!")

# Print all guesses at the end
print("All guesses:", guesses)

'''
#used CoPilot to help me write this, adidng types.lower and __name__ helped!
types = input(f"What type is debug_mode {debug_mode}?: ")

if types.lower() == type(debug_mode).__name__:
    print("Correct!")
else:
    print("False, try again!")
'''