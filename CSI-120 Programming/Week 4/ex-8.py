#Checking Age Eligibility to work (Age must be between 18 and 67)

import os

os.system('cls')

age = int(input("Please enter your age: "))

if 18 <= age <= 67:

    print(f"Age {age} is eligible to work.")

else:

    print(f"Age {age} is not eligible to work.")