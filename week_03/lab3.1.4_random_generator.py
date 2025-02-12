# lab3.1.4_random_generator.py
# Prints out a random number between 1 and 10. IMPORT MODULE RANDOM
# Author: Faolán Hamilton

import random

number = random.randint (1,20)
print ("Here is a random number {}" .format(number))

#Modified for user input range
'''
range_start = int(input("Input the first number in the range e.g. 1 in 1 -100: "))
range_end = int(input("Input the last number in the range e.g. 100 in 1 - 100: "))
number = random.randint (range_start, range_end)
print ("Here is a random number {}" .format(number))
'''