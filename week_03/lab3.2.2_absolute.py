# lab3.2.2_absolute.py
# Takes a number and gives the absolute value e.g. -4.0 = 4.0
# Author: Faolán Hamilton

# Give the absolute value of a number 
#Havind tried both int and float for this section, float works best as if the user inputs '3',
#float will generate 3.0 whereas in int if a user inputs 3.0 they will get an error.
#It's best to make it easiest for the input user to avoid them triggering an error.

number = float(input ("Enter a negative number e.g. -3.1: "))
absolute_value = abs(number)
print ('The absolute value of {} is {}' .format(number, absolute_value))
