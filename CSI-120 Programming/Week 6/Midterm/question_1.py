# Write a Python program that calculates an employee's bonus based on their years of service in a company.
# The program should:
# Ask the user to enter their years of service (as an integer).
# Determine the bonus percentage based on the following conditions:
# Less than 3 years → No bonus (0%)
# 3 to 5 years → 10% bonus
# 6 to 10 years → 20% bonus
# More than 10 years → 30% bonus
# Ask the user to enter their current salary (as a float).
# Calculate and display the bonus amount and total salary after the bonus.

years_of_service = int(input("Enter years of service: "))
current_salary = float(input("Enter current salary: "))

if years_of_service < 3:
    bonus_percentage = 0.00
    print(f"Bonus: {bonus_percentage * 100}%.")
elif years_of_service >= 3 and years_of_service <= 5:
    bonus_percentage = 0.10
    print(f"Bonus: {bonus_percentage * 100}%.")
elif years_of_service >= 6 and years_of_service <= 10:
    bonus_percentage = 0.20
    print(f"Bonus: {bonus_percentage * 100}%.")
else:
    bonus_percentage = 0.30
    print(f"Bonus: {bonus_percentage * 100}%.")

# Calculate the bonus amount and new salary
bonus_amount = current_salary * bonus_percentage
new_salary = current_salary + bonus_amount

# Display the results with two decimal places
print(f"Bonus Amount: ${bonus_amount}")
print(f"Total salary after the bonus ${new_salary}")
