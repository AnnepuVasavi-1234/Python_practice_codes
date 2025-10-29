#Generate a random number
#Loop
 #Ask the user to make a guess
 #if not a valid number
 #print error
 #....

import random

number_to_guess = random.randint(1,100)
while True:
    try:
        guess = int(input('Guess the number between 1 and 100: '))
        if guess > number_to_guess:
          print("Too high!")
        elif guess < number_to_guess:
          print("Too low!")
        else:
            print("Congratulations!..guessed correct")
            break
    except ValueError:
        print("Pls enter a valid number")

