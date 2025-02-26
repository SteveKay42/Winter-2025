#Create a program in python using while loop to replicate the following matrix 
#1 2 3 4 5

#50 51 52 53 54

#540 541 542 543 544

#5440 5441 5442 5443 5444

#54440 54441 54442 54443 54444

counter = 0
start_num = 1

while counter < 5:
    num = start_num
    while num < start_num + 5:
        print(num, end=" ")
        num += 1
    print()
    start_num = (start_num*10) + 40
    counter += 1
