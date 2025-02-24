num = int(input("Enter a number: "))
while num / 10 > 0:
    print(num % 10, end="")
    num = int(num / 10)
