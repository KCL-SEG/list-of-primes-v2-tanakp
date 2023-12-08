"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be a positive integer")
    current_number = 2
    while len(list) < number_of_primes:
        is_prime = all(current_number % i != 0 for i in range(2, int(current_number**0.5) + 1))

        if is_prime:
            list.append(current_number)
        
        current_number += 1


    return list

