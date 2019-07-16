import time

while True:
    input("You are Ollie, a likeable young guy in search of love. Our story begins when Ollie comes across an attractive young woman on Tinder...")
    print('----------------------------------------------------------------------------------------------------------')
    swipe_choice = input("Will you swipe left or right? 1)Right 2)Left \n").lower().strip()
    if swipe_choice == 'right':
        print("She swiped right, too! It's a match! Now don't screw this up..")
    elif swipe_choice == 'left':
        print("Hmm, perhaps Ollie's standards are a little high... GAME OVER")
        break
    print('_________________CHAPTER 2_______________')
    print('')
    print("She messages you and asks for a date! But she wants you to pick the type of restaurant.")
    food = input("What kind of food will you choose?: (1)Italian (2)Curry (3)Pub grub \n").lower()
    if food == 'italian':
        print("Ah, molto bella!")
    elif food == 'curry':
        print("Curry on a first date!? What were you thinking? GAME OVER")
        break
    elif food == 'pub grub':
        print("Lovely jubbly.")

    print('_________________CHAPTER 3_______________')
    print('')
    drunk_guess = input("You meet at the restaurant and after an hour, everything seems to be going fine! However, you notice your date might have had a bit much to drink... what do you think? (Enter true or false) \n").lower().strip()
    input("Whatever you say! Oh no, now she's asking how old you think she is! Maybe she's had too much drink to really notice what you say...")
    age_guess = int(input("What age will you say? \n"))

    if age_guess < 30 or drunk_guess == 'true':
        print("She smiles and shrugs. 'I'll never tell!' Phew, that was a close one!")
    else:
        print("Uh, I think you might have miscalculated somewhere... GAME OVER")
        break

    print('_________________CHAPTER 4_______________')
    print('')
    print("The rest of the evening goes wonderfully and soon, the bill arrives. Yikes! £100!?")
    pay_choice = input("What will you do?: (1)Say you left your wallet at home. (2)Offer to pay. \n")
    money_in_wallet = int(input("Wait... how much money do you actually have? \n"))

    if pay_choice == 'offer' and money_in_wallet >= 100:
        input("How very gallant of you! She seems impressed...")
        input("You've got a date!")

    else:
        print("Sorry, nobody likes a cheapskate.")
        break

