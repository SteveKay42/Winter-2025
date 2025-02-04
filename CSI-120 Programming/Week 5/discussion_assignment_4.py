# Display first n prime numbers

# Accepts user input for how many prime numbers to display
num_primes_to_display = int(input("Enter the number of prime numbers to display: "))

# Initialize variables
current_number = 2  # Start checking for prime numbers from 2
primes_found = 0  # Counter for the number of prime numbers found

# Loop until the desired number of prime numbers is found
while primes_found < num_primes_to_display:
    divisor = 2  # Start checking divisors from 2
    is_prime = True  # Assume current_number is prime until proven otherwise

    # Check if current_number is divisible by any number from 2 to current_number // 2
    while divisor <= current_number // 2:
        if current_number % divisor == 0:  # If current_number is divisible by divisor, it is not prime
            is_prime = False
            break  # Exit the loop if a divisor is found
        divisor += 1  # Increment divisor to check the next potential divisor

    # If no divisors were found, current_number is prime
    if is_prime:
        print(current_number)  # Print the prime number
        primes_found += 1  # Increment the count of prime numbers found

    current_number += 1  # Check the next number in the next iteration