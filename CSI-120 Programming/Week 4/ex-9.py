# Validating user's login credentials

import os

os.system('cls')

# Predefined username and password

correct_username = "user123"

correct_password = "securePassword!2024"



# Prompt the user to enter their username and password

entered_username = input("Enter your username: ")

entered_password = input("Enter your password: ")



# Check if the entered credentials match the predefined ones

if entered_username == correct_username and entered_password == correct_password:

    print("Login successful!")

else:

    print("Invalid username or password. Please try again.")