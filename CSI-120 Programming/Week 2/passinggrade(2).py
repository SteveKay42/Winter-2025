#Create a program that accepts user's score and checks if student passed the class, Minimum passing score is 73.
#Input value:
score = int(input("Enter Test Score: ")) #for example, if the input is 78, it will not be a number, rather it will be string representation of a number. So, make sure, if you are using a number as input, convert it into appropriate data type.

# check is input is between 0 and 100
if score <=100 and score >=0:
    #Compare if the input is minimum 73
    if score >=73:
        print("The student has passed!")
    else:
        print("The student has failed.")
else:
    print("Out of range.")