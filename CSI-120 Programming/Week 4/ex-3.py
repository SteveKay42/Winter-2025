#Check if a Random Number is in a Specific Range



import random,os

os.system('cls')




# Generate a random number between 1 and 100

random_number = random.randint(1, 100)



# Define the specific range

lower_bound = 20

upper_bound = 50



# Check if the random number is within the specified range

if lower_bound <= random_number <= upper_bound:

    print(f"The random number {random_number} is within the range {lower_bound} to {upper_bound}.")

else:

    print(f"The random number {random_number} is outside the range {lower_bound} to {upper_bound}.")