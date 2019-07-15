# # Data types
#     # Computers are stupid.
#     # They dont understand context, and we need to be specific with data types
#
# # We can use type() to check data types
#
# # Strings
#     # Lists of characters bundled together in a specific order
#         # using index
# print('hello')
# print (type('hello'))
#
#     # Concatination of strings - joining of two or more strings
# string_a = 'hello there'
# name_person = 'Juan Pier'
# print(string_a + ' ' + name_person)
#
# # Useful methods
# # Length
# print(len(string_a))
# print(len(name_person))
#
# # Strip
# # removes trailing white spaces from either front or the end
# string_num = ' 90383 '
# print(type(string_num))
# print(string_num)
# print(string_num.strip())

# Split - It is a method for strings
# It splits in a specific location and output a list (data type)
string_text = "Hello, my name is Shav, I like cars"
split_string = string_text.split(' ')
split_string = string_text.split()
split_string = string_text.split('e')
print(split_string)

# Count / Lower / Upper / Capitalise
text_example = "here is sOMe text, with lot's of text"
# Count
print(text_example.count('e'))
print(text_example.count('text'))

# Lower
print(text_example.lower())

# Upper
print(text_example.upper())

# Capitalise - capitalises the first letter in the string
print(text_example.capitalize())
print('PizzaHut'.capitalize())
print('  PIZZAHUT'.strip().capitalize())
print('PIZZA HUT'.capitalize())
print('Pizza Hut'.capitalize())

# Get user input and print first and last name
# - get user input / first name
# - Save user input to variable
first_name = input ('What is your first name?')
# - Get user last name
# - and save it to variable
last_name = input ('What is your last name?')
# - Join the two and
    # let us use concatination
full_name = first_name + ' ' + last_name
print(full_name)
    # let us use interpolation - use f behind the string to recognise python code
welcome_message = f"Hi {full_name}, you are very welcome!"
print(welcome_message)


# - print






# Casting











