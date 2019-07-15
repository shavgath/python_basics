# Booleans
# Boolean is a data type that is either true or false

#Syntax is capital letter
var_true = True
var_false = False

print(type(var_true))
print(type(var_false))

# When we equate / evaluate something we get a boolean as a response
# == / != / <> / >= / <=
weather = 'Rainy'

print(weather == 'Sunny')
print(weather == 'Rainy')

# Logical **AND** & **OR**
# Evaluates two sides, and BOTH have to be true for it to return True
print('testing logical and: ')
print(weather == 'Rainy' and weather == 'Sunny')
print(True and True)

# True
print(weather == 'Rainy' and weather == 'Rainy')
print(True and True)

# Logical OR - One of the side of the equation have to be True to return True
print('>Testing logical or: ')
print(True or False)
print(False or False)

# Some methods or functions can return booleans
potential_number = '10'
print(potential_number.isnumeric())

text = 'Hello World!'
print(text[0] == 'H')
print('Testing .startswith(arg)')
print(text.startswith('H'))
print(text.startswith('h'))
print('Testing .endswith(arg)')
print(text[-1] == '!') # string are list of character. -1 represents the last index in set list
print(text.endswith('!'))
print(text.endswith('?'))

# Booleans and numbers
print("printing bool values of numbers")
print(bool(0))
print(bool(1))
print(bool(13))
print(bool(-1))
print(bool(3.14))
print('complex')
print(bool(1+3j))

# Value of none
print(bool(None))
