# Lists and Dictionaries
# List aka: array

# Sometimes we just need to list our crazy x-pokemons :
# because we don't want to work there

# this is how you make a list
# [] separate items using ,
# ['bananas', 'pine', 'gasoline']
# declaring a list and saving to variable
crazy_pokemons = ['Snorlax', 'Jigglipuff', 'Mewtoo']

print(crazy_pokemons)
print(type(crazy_pokemons))
# Lists are organised using index
# [    0     ,   1   ,      2    ]
# ['bananas', 'pine', 'gasoline']
# Indexes start at 0

print(len(crazy_pokemons))
print(crazy_pokemons[2])
# print first in the list
print(crazy_pokemons[0])

# If you want to print the last in a list
# you have two options
    # array[len(array) - 1]
print(crazy_pokemons[len(crazy_pokemons)-1]) # OR
print(crazy_pokemons[-1])

# Re-assigning the value in a list, using the index
# We need to evolve Mewtoo to Mewtree
print(crazy_pokemons)
crazy_pokemons[2] = 'Mewtree'
print(crazy_pokemons)

# Appending a new pokemon
# We caught Pigeotto
crazy_pokemons.append('Pigeotto')
print(crazy_pokemons)

# Inserting with index numbers
crazy_pokemons.insert(0, 'Rattata')
print(crazy_pokemons)
crazy_pokemons.insert(2, 'Pikachu')
print(crazy_pokemons)

# Removing a record - using index
# removes item from last index
crazy_pokemons.pop()
print(crazy_pokemons)

#removes item in first index
crazy_pokemons.pop(0)
print(crazy_pokemons)

# Removing - using a value
crazy_pokemons.remove('Snorlax')
print(crazy_pokemons)

# List can have any data types

mixed_list = ['Jones', 10, 42, 'John']
print(mixed_list)
print(type(mixed_list[0]), type(mixed_list[1]))

# Inception list
#     # [   0   , 1 ,  2   ,  3]
leo_d = ['first', 2, ['leo', 'd']]

print(leo_d[0][1])
print('accessing the index 2')
print(leo_d[2])
sub_array = leo_d[2]
print(sub_array)
print(sub_array[1])

# ALL of this is the same as
print(leo_d[2][1])

# Accessing 'e' in leo
print(leo_d[2][0][1])

print('__________________________')

# Tuples
# Tuples are Immutable lists
# Meaning they do not change
# Syntax
    # tuple_list = ('hello', 10, 13, 4)
my_tuple = ('eggs', 'bread', 'oats', [11, 13])
print(my_tuple)
print(type(my_tuple))

breakpoint()

# We cannot change the tuple itself, but we can change the state of items inside
# We cannot re-assign them


