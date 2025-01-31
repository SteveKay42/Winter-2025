more = "y"
while more.lower() == "y":
    miles_driven = float(input("Enter miles driven: "))
    gallons_used = float(input("Enter gallons of gas used: "))

   #validate input
    if miles_driven <= 0 or gallons_used <= 0:
        print("Both entries must be greater than zero. Please try again.")
        continue
    mpg = round(miles_driven / gallons_used, 2)
    print("Miles per gallon:", mpg, "\n")
   
    more = input("More entries? (y/n): ")
    print()

print("Okay, bye!")