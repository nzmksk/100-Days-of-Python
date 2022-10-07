# The prime factors of 13,195 are 5, 7, 13, and 29.
# Create a function that returns the largest prime factor of a given number.

def largest_prime_factor(number):
    biggest_prime_factor = 2
    def factors(number):
        odd_factors = []
        for odd_number in range(3, (number + 1), 2):
            if number % odd_number == 0:
                odd_factors.append(odd_number)
        return odd_factors
    for i in factors(number):
        if len(factors(i)) == 1:
            if biggest_prime_factor < i:
                biggest_prime_factor = i
    return biggest_prime_factor


# My current algorithm is quite slow, considering it iterates every odd number starting from 3 to the maximum odd value.
# One method to simplify the algorithm is to use the lowest factor to find the highest factor, and determine whether the highest factor
# is a prime number. If otherwise, the function is repeated to find the next highest factor, until the highest prime factor is found.

# Will look into this again in the future.