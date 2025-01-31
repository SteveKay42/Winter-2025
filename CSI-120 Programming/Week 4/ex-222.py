#Generate two random numbers between a user-identified range, have the computer generate two numbers within this range, and identify which number is bigger, smaller, or equal
#Expected output: 
#Enter beginning of the range:
#Enter ending of the range:
#Generated Number_1: 7
#Geneated Number_2: 9
#Number 9 is larger than Number 7

import os, random
os.system('cls')

begin_1 = int(input("Enter the beginning number of the range: "))
end_2 = int(input("Enter the ending number of the range: "))
number_1 = random.randint(begin_1, end_2)
number_2 = random.randint(begin_1, end_2)

if number_1 > number_2:
    print(f"Number {number_1} is larger than Number {number_2}")
elif number_1 == number_2:
    print(f"Number {number_1} is equal to Number {number_2}")
else:
    print(f"Number {number_2} is larger than Number {number_1}")
