# import random
from random import randint    # We use this instead of import random so it is commented above
import art
print(art.logo)
# numbers=list(range(1,101))   #This is a part of import random module so commented here due to additional method

def play_game():
    print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
    # computer_guess = random.choice(numbers)
    computer_guess=randint(1,100)
    def ranges():
        if guess < computer_guess:
            print("Too low.\nGuess Again.\n")
        elif guess > computer_guess:
            print("Too high.\nGuess Again.\n")

    # attempts = 10 if level == "easy" else 5   #Shortcut method but if user enters invalid level then also works as high level
    attempts=0
    if level=="easy":
        attempts=10
    elif level=="hard":
        attempts=5
    else:
        print("Invalid Level Chosen! Please Choose From the Given Options correctly")
        exit()
    while attempts:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if computer_guess == guess:
            print(f"You got it! The answer was {computer_guess}")
            exit()
        else:
            attempts -= 1
            ranges()
    print(f"You've run out of guesses! The answer was {computer_guess}. Refresh page to run again ")

play_game()