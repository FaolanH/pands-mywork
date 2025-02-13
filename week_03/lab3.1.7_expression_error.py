#labs3.1.7_experssion_error.py
#Why does this expression cause an error? and fix it (use''' ''')
#Author: Faolán Hamilton

'''
message = 'I have eaten ' + 99 + 'burritos.'
print(message)


#I think because it's trying to add a str and int

message = 'I have eaten ' + '99' + ' burritos.'
print(message)



#You can also do it this way to make sure it doesn't error

message = f'I have eaten {'99'} {'burritos.'}'
print(message)

'''
#eggs is a valid variable name bacause it is a string, 100 is an integer


#What three functions can be used to get the integer, floating-point number, or 
#string version of a value?

#int(), float(), str() ???

x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))