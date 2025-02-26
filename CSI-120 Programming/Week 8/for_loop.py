#for i in range(1,25):
    #if i % 5 == 0:
        #continue
    #print(i, end="   ")
    
#print("End of the program")

num = int(input("Enter starting number: "))
counter = 0
total = int(input("Enter total count: "))
while counter < total:
    if num % 5 == 0:
        num += 1
        continue
    print(num, end="   ")
    num += 1
    counter += 1

print("\nTotal numbers: ", counter)
