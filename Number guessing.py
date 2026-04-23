import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0
guess = None

print(" Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")

# Game loop
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low ")
    elif guess > secret_number:
        print("Too high ")
    else:
        print(" Congratulations! You guessed the number!")
        print(f"It took you {attempts} attempts.")