import random

def guess_the_number():
    number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0

    print("Welcome to 'Guess the Number'!")
    print("I've picked a number between 1 and 100. Try to guess it.")

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():  # Check if input is a number
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
            break

# Run the game
guess_the_number()