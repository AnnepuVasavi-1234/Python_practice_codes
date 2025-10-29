#Ask the user to make choivce
#if choice is not valid ---> print(not valid)
# valid 
#Let computer to make a choice --> print(emoji)
#Determine the winner
#Ask user like continue or not
# If not terminate

# \ it is used to tell the code of same line but we are writing it in next line

import random

choices = ('r','p','s')

while True:

    user_choice = input("rock,paper,scissor?(r/p/s): ").lower()
    if user_choice not in choices:
        print("not valid")
        continue

    computer_choice = random.choice(choices)

    print(f'you choose {user_choice}')
    print(f'computer choose {computer_choice}')

    if user_choice==computer_choice:
    print("You win")
    elif(
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')  ):
        print("You win")

    else:
    print("you lose")

    should_continue = input('continue(y/n): ').lower()
    if should_continue == 'n':
        break 


# ✅ To Indent (move right by one tab):
# - Select the lines you want to indent.
# - Press Tab.

# 🔙 To Unindent (move left by one tab):
# - Select the lines you want to unindent.
# - Press Shift + Tab.
