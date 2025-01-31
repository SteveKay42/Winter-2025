def calculate_percentage(total, amount):
    try:
        percentage = (amount / total) * 100
        return percentage
    except ZeroDivisionError:
        return "Total cannot be zero."

total = float(input("Enter the total amount: "))
amount = float(input("Enter the dollar amount: "))

percentage = calculate_percentage(total, amount)
print(f"The percentage is: {round(percentage, 2)}%")