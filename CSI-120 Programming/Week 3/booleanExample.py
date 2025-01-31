
import os

os.system('cls')

#Assign a boolean value to a variable
is_raining=True
print("The data type is: " + str(type(is_raining)))
#complete program by checking if it is raining, then display messag: take an umbrella!
#otherwise: display message: "enjoy the sunshine!"

is_raining = (input("Is it raining?: (y/n): "))

if is_raining:
    print("Take an umbrella!")
else:
    print("Enjoy the sunshine!")