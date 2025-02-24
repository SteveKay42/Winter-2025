#Game Description:
#The program generates a random 2-digit lottery number (between 10 and 99).
#The player enters a 2-digit guess.
#The program checks the guess and gives rewards based on the following rules:
#Exact match → "Congratulations! You won $10,000!"
#Same digits in different order → "Great job! You won $5,000 "
#One matching digit → "Good try! You won $1,000!"
#No match → "Sorry, better luck next time!

# Import the random module
import random

# Generate a random 2-digit lottery number (between 10 and 99)
lottery_number = random.randint(10, 99)

# Ask the player to enter a 2-digit guess
player_guess = int(input("Enter your 2-digit lottery guess (10-99): "))
print("The lottery number is:", lottery_number)

# Check if the player's guess matches the lottery number exactly
if player_guess == lottery_number:
    print("Congratulations! You won $10,000!")

# Check if the player's guess has the same digits in a different order
# player_guess % 10 extracts the last digit of the player's guess
# lottery_number // 10 extracts the first digit of the lottery number
# player_guess // 10 extracts the first digit of the player's guess
# lottery_number % 10 extracts the last digit of the lottery number
# This condition checks if the digits of the player's guess are the reverse of the lottery number
elif player_guess % 10 == lottery_number // 10 and player_guess // 10 == lottery_number % 10:
    print("Great job! You won $5,000!")

# Check if the player's guess has one matching digit
# player_guess % 10 extracts the last digit of the player's guess
# lottery_number % 10 extracts the last digit of the lottery number
# player_guess // 10 extracts the first digit of the player's guess
# lottery_number // 10 extracts the first digit of the lottery number
# This condition checks if any of the digits of the player's guess match the digits of the lottery number
elif (player_guess % 10 == lottery_number % 10 or player_guess % 10 == lottery_number // 10 or player_guess // 10 == lottery_number % 10 or player_guess // 10 == lottery_number // 10):
    print("Good try! You won $1,000!")
    
# If none of the above conditions are met, the player did not win
else:
    print("Sorry, better luck next time!")

