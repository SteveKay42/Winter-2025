# Write a Python program that asks the user to enter their exam score (0-100)
# And then prints their letter grade based on the following criteria:
# 90 - 100 → "A - Excellent!"
# 80 - 89 → "B - Good job!"
# 70 - 79 → "C - You Passed!"
# 60 - 69 → "D - Needs improvement!"
# Below 60 → "F - Failed. Try again!"
# If the user enters a number outside of 0-100, print "Invalid input. Please enter a score between 0 and 100."

# Ask the user to enter their exam score
exam_score = int(input("Enter your exam score (0-100): "))

# If the exam score is outside the range of 0-100, print an error message
if exam_score < 0 or exam_score > 100:
    print("Invalid input. Please enter a score between 0 and 100.")

# Check the exam score and print the corresponding letter grade
else:
    if exam_score >= 90:
        print("A - Excellent!")
    elif exam_score >= 80:
        print("B - Good job!")
    elif exam_score >= 70:
        print("C - You Passed!")
    elif exam_score >= 60:
        print("D - Needs improvement!")
    elif exam_score < 60:
        print("F - Failed. Try again!")
