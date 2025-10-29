import random


while True:
    choice = input("Roll the dice?(Y/N): ").lower()
    if choice == 'y':
        diel1 = random.randint(1,6)
        diel2 = random.randint(1,6)
        print(f'({diel1},{diel2})')
    elif choice == 'n':
        print('Thanks for playing')
        break
    else:
        print('Invalid choice!')



# Why while True: is used
# - Infinite loop until user exits
# while True: creates a loop that runs forever — unless we break out of it manually. This is perfect for interactive programs like dice games where we want to keep asking the user if they want to roll again.


# - for loop
# Not suitable here — for is best when you know how many times to repeat something.

