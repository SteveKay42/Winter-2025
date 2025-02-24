#for i in range(1,25):
    #if i % 5 == 0:
        #continue
    #print(i, end="   ")
    
#print("End of the program")

num = 1
counter = 0
total = 30
while counter < total:
    if num % 5 == 0:
        num += 1
        continue
    print(num, end="   ")
    num += 1
    counter += 1

print("\nTOtal numbers: ", counter)
