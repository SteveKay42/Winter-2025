# Accept user input

choice = "y"

while choice.lower() == "y":
    customer_name = input("Enter the first name: ")
    product_name = input("Enter product name: ")
    quantity = int(input("Please enter how many purchased: "))
    price = int(input("How much does your product cost?: "))
    total_amount = (quantity * price)

    print(f"{customer_name} has purchased {quantity} {product_name}'s for ${total_amount}.")
    choice= input("Do you want to continue? y/n: ")
print("Have a great day!")

