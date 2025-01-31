#Find the Largest of Three Random Numbers

import random,os

os.system('cls')



# Generate three random numbers

random_number1 = random.randint(1, 100)

random_number2 = random.randint(1, 100)

random_number3 = random.randint(1, 100)



# Find the largest of the three numbers

largest_number = max(random_number1, random_number2, random_number3)



# Display the result

print(f"The three random numbers are {random_number1}, {random_number2}, and {random_number3}.")

print(f"The largest number is {largest_number}.")