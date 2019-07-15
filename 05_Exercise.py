import datetime

print('What is your name?')
first_name = input()
print('What is your last name?')
last_name = input()
year = int(input('Enter the year you was born \n'))
month = int(input('Enter a month you was born \n'))
day = int(input('Enter a day you was born \n'))
dob = datetime.date(year, month, day)
print('Enter a funny fact about yourself..')
fact = input()

print()
print('Your name is',first_name, last_name)
print('........................,............')
print('You was born on',dob)
print('........................,............')
print('A funny fact about you is:',fact)
