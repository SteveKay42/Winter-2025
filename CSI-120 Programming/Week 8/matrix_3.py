#Create a program in python using while loop to replicate the following matrix 

#1 2 3 4 5

#30 31 32 33 34

#320 321 322 323 324

#3220 3221 3222 3223 3224

#32220 32221 32222 32223 32224

counter = 0
start_num = 1

while counter < 5:
    num = start_num
    while num < start_num + 5:
        print(num, end=" ")
        num += 1
    print()
    start_num = (start_num*10) + 20
    counter += 1
