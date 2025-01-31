#Create a program that accepts user's score and checks if student passed the class, Minimum passing score is 73.
#Input value:
score = int(input("Enter Test Score: ")) #for example, if the input is 78, it will not be a number, rather it will be string representation of a number. So, make sure, if you are using a number as input, convert it into appropriate data type.

#Compare if the input is minimum 73

if score >=73:
    print(f"Pass: Out of 100 student got {score}  scores.")
else:
    print(f"Fail: out of 100 student for {score} scores.")