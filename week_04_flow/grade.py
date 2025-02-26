#grade.py
#Read in a student's percentage mark and print out corresponding grade (program must ensure % is valid)

# Under 40% => Fail 
# Between 40% and 49%  => Pass 
# Between 50% and 59%  => Merit 2 
# Between 60% and 69%  => Merit 1 
# Over 70%    => Distinction

#Author: Faolán Hamilton

#Need to learn loops to modify/keep prompting user to enter more titles 
# How would you use a while loop to modify 1 so that it keeps prompting the 
#user for a number until the user enters -1 

#datacamp flow control if elif else 

percentage = float(input("Please enter the student's percentage (without the % sign): "))
#print (f"{percentage} %") #(prints whole number, must have % symbol)

grade = round(percentage)

if grade < 0 or grade > 100:
    print ("Please input a number between 0 and 100")

elif grade < 40: #greater than 0 but less than 40
    print ("Fail")

elif grade < 50: # between 40 and 49
    print ("Pass")

elif grade < 60: # between 50 and 59
    print ("Merit 1")

elif grade < 70: # between 60 and 69
    print ("Merit 2")

else: # between 70 and 100
    print ("Distinction")

