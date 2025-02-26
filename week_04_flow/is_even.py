#is_even.py
#user inout a number, tell user if number is odd or even
#Author: Faolán Hamilton

num = int(input("Please enter an integer (a whole, postiive number): "))

if (num % 2) == 0:
    print (f"{num} is an even number.")

else:
    print(f"{num} is an odd number.")