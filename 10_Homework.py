story = {
    'hero': ['turtle'],
    'beginning': 'Once there was a hare who wanted to race a turtle' ,
    'middle': 'The turtle took its time, while the hare rushed itself towards the finish line.',
    'end': 'In the end the turtle won. Moral of the story is that the slow and steady wins the race.',

}

print(story['beginning']),
print(story['middle']),
print(story['end']),
print(story['hero'])

decision = input('Would you like to change the hero? (Y/N)')
if (decision.upper() == 'Y'):
    character = input('What character would you like to replace it with?')
    story['hero'] = character
    new_begin = story['beginning'].replace('turtle',character)
    new_middle = story['middle'].replace('turtle', character)
    new_end = story['end'].replace('turtle', character)
    print(new_begin)
    print(new_middle)
    print(new_end)

print('')
print('------------------------ THE END -------------------------------------------------')








