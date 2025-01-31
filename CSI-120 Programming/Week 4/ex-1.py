#Check if a random number is even or odd
import os, random
os.system('cls')
#generate a random number

number = (random.randint(1,100)) #This is calling a library and its function: random library and rand.int function
#print("Sytem generated number = " +str(number))
print(f"System generated number is {number}")
if number % 2 == 0:         #check number is even. If remainder after dividing a number by 2 is 0, then it's an even number.
    print("Number is even")
else:
    print("Number is odd")