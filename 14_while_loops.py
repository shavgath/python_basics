# While loops

# Syntax
# While <condition>
    # Block of code
    # **Optional** if <condition>
#                        break

# counter = 0
#
# while counter < 28:
#     print("Let's go out! My age is: ", counter)
#     counter += 1
#
# print('End')

while True:
    print('Welcome to the loop')
    word = input('Tell me a word \n')
    # break # - 
    if word == 'bananas':    # condition to go into the break key word
        print('you cracked the code')
        break    # Safe word to break the loop
    else:
        print("HAHAHAHAHA YOU FOOL. YOU WILL NEVER LEAVE")
        print("AHAHAHA")

