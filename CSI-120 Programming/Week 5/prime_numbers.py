#Display first n prime numbers
#display first 10 prime numbers
import os
os.system('cls')

num = int(input("Enter number: "))
i = 2
flag = False
counter = int(input("Enter number: "))
count = 0

while count < counter:
    while i < num: 
        if num % i == 0:
            flag = True
            break
        i = i + 1
    if flag == False:
        print(num)
    num = num + 1
    count = count + 1