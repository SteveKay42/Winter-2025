#Generate the number and also accept the input from the user, skip out from the loop as soon as random number matches with the number provided by the end user.
#System generates 99, user inputs 300. System should stay in the loop until the user input and the random number matches.

import random

while True:
    num = int(input("Enter a number between 1 and 5: "))
    random_num = random.randint(1, 6)
    if num == random_num:
        print("They match! Random number:", random_num, "User number:", num)
        break

