import random

random_number1 = random.randint(1, 100)
random_number2 = random.randint(1, 100)

if random_number2 != 0 and random_number1 % random_number2 == 0:

    print(f"The random number {random_number1} is divisible by {random_number2}.")

else:

    print(f"The random number {random_number1} is NOT divisible by {random_number2}.")