# For loop - Using dictionaries / Hashes

# Syntax
# for <placeholder> in <dict>:
    # run block of code

# dict_data = {
#     'name': 'Bronson',
#     'money': 200,
# }

# We use the key to access the values of our dictionary
# print(dict_data['name'])
#
# for key_placeholder in dict_data:
#     # When we iterate over a hash/dictionary
#     # the placeholder, holds an individual key during each iteration
#     print(key_placeholder) # THIS is the key
#     value = dict_data[key_placeholder] # use key and dictionary to extract individual value of a key
#     print(value)
#
# dict_data = {
#     'name': 'Bronson',
#     'money': 200,
# }
#
# for key_place_holder in dict_data:
#     print(key_place_holder + ':', dict_data[key_place_holder])

dict_data = {
    'name': 'Bronson',
    'money': 200,
}

embedded_dict_data = {
    1:{
        'name': 'Bronson',
        'money': 200
    },
    2:{
        'name': 'Tania',
        'money': 300
    },
    3:{
        'name': 'Tylor',
        'money': 400
    }
}

for key in embedded_dict_data:
    print(key)
for item in embedded_dict_data.values():
    print(item)
    print(type(item))