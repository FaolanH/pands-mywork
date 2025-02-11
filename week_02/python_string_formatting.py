#python_string_formatting.py
#messing around to produce different outputs as found on Python String Formatting
#Author: Faolán Hamilton

#F-Strings
#interestingly, with this simple format below using the f or not does not impact the ouput, 
#presumably more important in longer strings
'''
text = f"My name is Faolán"
print(text)

#Placeholders and Modifiers
#Interestingly, using my name FaolánH with no quotes brings an error, but not for a number...
name = "FaolánH"
text = f"My name is {name}"
print (text)


#Modifiers - 2 decimal places
price = 22
text = f"The price is {price:.2f} euros"
print(text)

#or don't define price (aka variable) and add it in 
text = f"The price is {63:.2f} euros"
print (text)


#Perform operations in F-Strings
#I like to see thousand separator, I add ':,' (Source: https://blog.finxter.com/5-best-ways-to-format-numbers-with-thousand-separators-in-python/)
text = f"The price is {17*84:,} euros"
print (text)

#math operations on variables
price = 78
tax=0.23
text = f"The price is {price +(price*tax)} euros"
print (text)

#if...else statements
price = 16
text = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(text)
'''

#WANT TO CONTINUE PRACTISING? START AT EXECUTE FUNCTIONS IN F-STRING