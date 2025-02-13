# lab3.3.3_normalize.py
# convert string to lower case
# Author: Faolán Hamilton

input_string = input("Please enter a string (any character/number of characters): ")
normalized = input_string.lower()

input_string_len = len(input_string)
normalized_len = len(normalized)

#output_message = ("We reduced the input string from {} to {} characters." 
#.format(input_string_len, normalized_len))
#instead of format at end, put into {} in text

print (f"That string normalized is: {normalized}")
print (f"We reduced the input string from {input_string_len} to {normalized_len} characters.")
