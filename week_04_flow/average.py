#average.py
#keeps reading numbers until user enters 0, append each into a list. Otput = each number + average
#Author: Faolán Hamilton

#this will be my list of numbers to print
numbers = []

#first number to be input
number = list(input("Please enter a number (press 0 to quit): "))

#ensures 0 = quit
while number != 0:
    numbers.append(number)

    # next number 
    number = int(input("Please enter another number (press 0 to quit): "))

for value in numbers:
    print (value)

average = float (sum(numbers)) / len(numbers)
print (f"The average of the numbers is {average}.")