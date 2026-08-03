import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        user_guess = input("Guess a number between 1 and 100: ")
        
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        user_guess = int(user_guess)
        attempts += 1
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break
        
number_guessing_game()