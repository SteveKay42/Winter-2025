#Create a program in python using while loop to replicate the following matrix 
#1 2 3

#3 4 5

#5 6 7

counter = 0
start_num = 1
while counter < 3:
    num = start_num
    while num < start_num + 3:
        print(num, end=" ")
        num += 1
    print()
    start_num += 2
    counter += 1