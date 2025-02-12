# lab3.1.3_div.py
# Reads in two numbers (inputs), divides the first by the second to give integer results AND remainder
# Author: Faolán Hamilton

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) # the int and // gives the int division, so it's not a float and /
remainder = x%y 

print ("{} divided by {} is {} with remainder {}" .format ( x, y, answer, remainder))