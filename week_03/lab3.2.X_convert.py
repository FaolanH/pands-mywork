# lab3.2.X_convert.py
# take an input of an amount in the form -9.44 (9 dollars and 44 cent) and output the amount in cent, (944)
# aka, take in a float amount of dollars and returns that absolute amount in cent. 
# Author: Faolán Hamilton


euros = float(input("Please enter and amount e.g. 9.45: "))
cents = abs(euros)
print ('{} in cents is {}' .format (euros, cents))