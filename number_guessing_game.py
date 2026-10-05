import random
secret_number = random.randit(1, 10)
print("welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
guess = int(input("enter your guess: "))
if guess == secret_number:
  print("correct! You guessed the number!")
elif guess < secret_number:
  print("Too low!")
else:
  print("Too high!")
