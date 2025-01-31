#Generate two numbers between x and y and accept another range and tell if the generated number is within that range.
import os, random
os.system("cls")
#input beginning of the range_1
begin_1 = int(input("Enter beginning of the range: ")) #100
#input end of the range
end_1 = int(input("Enter the end of the range: ")) #1000
number = random.randint(begin_1, end_1)

#Enter beginning range_2:
begin_2 = int(input("Enter beginning of the range: ")) #100
#Enter ending range:
end_2 = int(input("Enter the end of the range: ")) #1000

if number >= begin_2 and number <=end_2: #To combine two expression, use logical operator
    print(f"The generated number, {number}, is within the range.")
else:
    print(f"The generated number, {number}, is not within the range.")


