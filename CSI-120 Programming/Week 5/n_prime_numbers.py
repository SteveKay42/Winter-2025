# Display first n prime numbers

def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def find_n_primes(n):
    """Find and return the first n prime numbers."""
    primes = []
    current_number = 2
    while len(primes) < n:
        if is_prime(current_number):
            primes.append(current_number)
        current_number += 1
    return primes

def main():
    """Main function to execute the prime number finding."""
    # Accepts user input for how many prime numbers to display
    num_primes_to_display = int(input("Enter the number of prime numbers to display: "))

    # Find and display the first n prime numbers
    prime_numbers = find_n_primes(num_primes_to_display)
    print(prime_numbers)

if __name__ == "__main__":
    main()