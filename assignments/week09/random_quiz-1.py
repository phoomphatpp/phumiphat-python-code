"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
import random
random_guess = random.randint(1,20)
attempts = 6
print("=== SIMPLE GUESSING GAME ===")
print("Guess my number between 1 and 20!")
print(f"You have {attempts} attempts.")
    

for i in range(attempts):
    number_guess = int(input(f"Attempt {i+1} / 6 - enter you guess: "))
    if number_guess > random_guess:
        print("Too high! Try again.")
    elif number_guess < random_guess:
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You won in {i+1} attempts!")
        break