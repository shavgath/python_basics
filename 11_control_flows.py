# Syntax - INDENTATION MATTERS
# if (condition>:
    # Block of code
# else:
    # Block of code
#

age = 16
if age >= 70:
    print('You can do everything, Just take it easy!')
elif age >= 18:
    print('Your age is above 18. you can vote! :D')
elif age >= 16:
    print('You can buy the lottery and probably go to prison but your record will be cleaned after... ')
else:
    print('You are under age to vote')

weather = input('What is the weather like? \n').lower().strip()
if weather == 'rainy':
    print('Go get an umbrella! ')
elif weather == 'rainy and stormy':
    print('Take a jacket and take an umbrella')
elif weather == 'foggy':
    print('Take an umbrella just in case')
elif weather == 'sunny':
    print('Yaaay its ' + weather)
    print('You need some shades son!')
else:
    print('Live your best life. ')


