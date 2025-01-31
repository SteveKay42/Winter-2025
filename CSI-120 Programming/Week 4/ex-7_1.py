# Checking If a Number is Even and Greater Than 10. 

#If both conditions are true then display: The number [number] is even and greater than 10.

# otherwise display: The number [number]] is either odd or not greater than 10.

import os

os.system('cls')

# Prompt the user to enter a number and convert the input to an integer

num = int(input("Enter a number: "))



# Check if the number is even and greater than 10

if num % 2 == 0 and num > 10:
    print(f"The number {num} is even and greater than 10.")
elif num % 2 != 0 and num > 10:
    print(f"The number {num} is odd and greater than 10.")
elif num % 2 != 0 and num < 10:
    print(f"The number {num} is odd and less than 10.")
elif num % 2 == 0 and num < 10:
    print(f"The number {num} is even, but less than 10.")
elif num == 10:
    print(f"The number {num} is even, but is equal to 10.")