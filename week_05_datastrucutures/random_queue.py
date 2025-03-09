#random_queue.py
#generate 10 random numbers, outuput as list 
#Author: Faolán Hamilton

import random 
queue = []
number_of_numbers = 10

for n in range (0,number_of_numbers):
    queue.append(random.randint (1,101))

print (f"the queue is now {queue}")

while len(queue) != 0:
    current_number = queue.pop(0)
    print (f"current number is {current_number} and the queue is {queue}")

print ("The queue is now empty")