"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


from random import randint
SOLUTION = randint(0, 10)
users_guess = ""
guess_count = 0
guess_limit = 4
guess_reached = False


# Kick off the program by calling the start_game function.
intro = ("Welcome to The Number Guessing Game!")
def start_game():
    print(intro)
start_game()
print("_" * len(intro))

print("Try to guess the secret number between 1-10?")

while users_guess != SOLUTION and not(guess_reached) and guess_count < guess_limit:
    try:
        users_guess = int(input("Enter your guess? "))
        if users_guess < 1 or users_guess > 10:
            print("Sorry, please pick a number between 1-10")
        guess_count += 1
    except ValueError:
        print("Sorry, please input a number?")    
    else:
        if users_guess < SOLUTION:
            print("Not quite, it's higher. Try again?")
        elif users_guess > SOLUTION:
            print("Not quite, it's lower. Try again?")
        else: 
            guess_reached = True
        
if not(guess_reached):
    print("Whomp Whomp Whomp, Sorry out of guesses, game is over!")
else:
    print("Wow you guessed the number in {} tries. Great job, game is over!".format(guess_count))


    
   

