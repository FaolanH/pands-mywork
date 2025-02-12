# lab3.1.5_randomfruit.py
# Print out a random fruit list format
# Author:Faolán Hamilton

import random

fruits = ['Apple', 'Cherry', 'Lemon', 'Kiwi', 'Mango', 'Banana', 'Orange', 'Grape', 'Pear', 'Pineapple']

#Random number between 0 and length-1 - the list starts from 0, or from the end at -1. 
#The computer does not read the fruits, rather their position in the list 
index = random.randint (0,len(fruits)-1)

fruit = fruits[index]
print("A random fruit: {}" .format(fruit))