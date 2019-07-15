# Dictionaries AKA Hashes
# work with key: value pairs.
# as opposed to using indexes

# Declaring a hash / dictionary
pika = { }

# Dictionaries work with keys: values
pika = {
    'name': 'Derik Dice',
    'pokemon': 'pikachu',
    'age': 17,
    'personality': 'Grumpy'
}

print(pika)
print(type(pika))
# Access information using the keys
print(pika['age'])
print(pika['pokemon'])

#Re assign values, using the keys
pika['age'] = 18
print(pika['age'])

# Adding a key: value pair
pika['colour'] = 'Yellowish'
print(pika)

# Creating key value for first & last name
full_name = pika['name'].split()
print(full_name)
first_name = full_name[0]
last_name = full_name[1]
print(first_name + ' ' + last_name)
pika['first_name'] = first_name
pika['last_name'] = last_name
print(pika)

# Embedded data
pika = {
    'name': 'Derik Dice',
    'pokemon': 'pikachu',
    'age': 17,
    'personality': ['grumpy', 'jumpy', 'shocking', 'static']
}
print(pika['personality'])
print(pika['personality'][0])

pika = {
    'name': 'Derik Dice',
    'pokemon': 'pikachu',
    'age': 17,
    'personality': {
        'grumpy': 10,
        'lovely': 2
    }
}

print(pika['personality']['grumpy'])

# Important Methods
# Accessing keys (name)
print(pika.keys())
print(type(pika.keys()))
print(pika.keys())

# Accessing values
values = pika.values()
print(values)

