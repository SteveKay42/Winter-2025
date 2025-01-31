#Simulate a Random Dice Roll and Compare Results of two two rolls


# Simulate two random dice rolls and compare Result of two roll 

import random,os

os.system('cls')

roll1 = random.randint(1, 6)

roll2 = random.randint(1, 6)



# Compare the results

if roll1 > roll2:

    print(f"Roll 1: {roll1} is greater than Roll 2: {roll2}.")

elif roll1 < roll2:

    print(f"Roll 1: {roll1} is less than Roll 2: {roll2}.")

else:

    print(f"Both rolls are equal: Roll 1: {roll1} and Roll 2: {roll2}.")