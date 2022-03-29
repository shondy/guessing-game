"""A number-guessing game."""
from random import randint

# Put your code here
#step 1: computer choose a random num
num = randint(1, 101)
print(num)
guess = None 
user_try = 0
#compare guess vs num
name = input("Howdy, what's your name? \n")

while guess != num: 
    guess = input(f"{name}, I'm thinking of a number between 1 and 100. Try to guess my number. Type q to exit: ")
    user_try += 1
    if guess == "q":
        break
    guess = int(guess)
    if guess == num:
        print(f"Well done, {name}! You found my number in {user_try} trie(s).")
        break
    elif guess < num:
        print("Too low. Guess again! ")
    else:
        print("Too high. Guess again! ")
    

