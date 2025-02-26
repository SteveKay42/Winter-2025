num = int(input("Enter a number: "))
iterations = int(input("Enter iterations: "))
for i in range(0, iterations):
    print("Red\n")
    for j in range(1, num + 1):
        print(j, end=" ")
    print("\n")