import os
os.system('cls')
import random

num = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == num:
    print(f"You got the right answer!The answer is {num}.")
elif guess > num:
    print(f"Better luck next time! Your answer is greater than the answer, {num}.")
else:
    print(f"Better luck next time! Your answer is less than the answer, {num}.")