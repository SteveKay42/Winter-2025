# Initialize the variable against which the entire while loop is compared to: either True or False
choice = "y"

# Accept user input for various options while loop is True
while choice.lower() == "y":
    customer_name = ""
    while customer_name == "":
        customer_name = input("Enter the name: ")
        if customer_name == "":
            print("Please enter a valid customer name.")

    product_name = ""
    while product_name == "":
        product_name = input("Enter product name: ")
        if product_name == "":
            print("Please enter a valid product name.")

    quantity = 0
    while quantity <= 0:
        quantity = int(input("Please enter how many purchased: "))
        if quantity <= 0:
            print("Invalid input")

    price = 0
    while price <=  0:
        price = int(input("How much does your product cost?: "))
        if price <= 0:
            print("Invalid input")

    total_amount = (quantity * price)

    print(f"{customer_name} has purchased {quantity} {product_name}'s for ${total_amount}.")
    choice = input("Do you want to continue? y/n: ")

print("Have a great day!")