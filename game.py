"""A number-guessing game."""
from random import randint
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueOutOfRange(Error):
    """Raised when the input value out of range between 1 and 100"""
    pass

def game(user_name):
    num = randint(1, 101)
    print(num)
    guess = None 
    user_try = 0

    while guess != num: 
        guess = input("Your guess? ")
        user_try += 1
        try:
            if guess == "q":
                user_try = float('inf')
                break
            guess = int(guess)
            if guess == num:
                print(f"Well done, {user_name}! You found my number in {user_try} tries.")
                break
            elif guess < 1 or guess > 100:
                raise ValueOutOfRange({"message":"The number should be between 1 and 100. Guess again!"})
            elif guess < num:
                print("Too low. Guess again! ")
            else:
                print("Too high. Guess again! ")
        except ValueOutOfRange as e:
            details = e.args[0]
            print(details["message"])
        except ValueError:
            print("Please enter a valid number: ")
    return user_try

def check_answer():
    play = True
    name = input("Howdy, what's your name? \n")
    print(f"{name}, I'm thinking of a number between 1 and 100. Try to guess my number. Type q to exit: ")
    score = float('inf')
    while play:
        score = min(game(name), score)
        play_again = input("Play again? y/n: ")
        if play_again == 'n':
            play = False
    if score != float('inf'):
        # if user won at least in one game
        print(f'Your best score is {score}')

check_answer()


    


