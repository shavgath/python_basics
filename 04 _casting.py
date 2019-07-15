# Casting is when you change the data type of an object.
# We can cast strings into integers or
# Integers into strings

# Casting String class to Integer class
number_string = '10'
print(type(number_string))
# now changing to integer using int()
number_int = int(int(number_string))
print(type(number_int))

# Casting Integer class to String class
print("now let us do the same but for strings into integers")
number_int2 = 11
print(type(number_int2))

number_int2_str = str(number_int2)
print('this value is a ',type(number_int2_str))

