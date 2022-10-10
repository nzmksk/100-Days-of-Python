# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the nth prime number?

def prime_number(nth_term):
    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True

    def odd_prime(num):
        if is_prime(num):
            return num

    exponential_factor = 1
    odd_prime_sequence = []
    while True:
        max_iteration = nth_term * (2 ** exponential_factor)
        odd_prime_sequence = list(map(odd_prime, range(3, max_iteration, 2)))
        while None in odd_prime_sequence:
            odd_prime_sequence.remove(None)
        if len(odd_prime_sequence) + 1 < nth_term:
            exponential_factor += 1
        else:
            break

    prime_sequence = [2] + odd_prime_sequence
    if nth_term > 0:
        return prime_sequence[nth_term - 1]
    else:
        return 'Please enter a natural number only (from 1 to any positive integer)'

# Test cases
# print(prime_number(6)) return 13
# print(prime_number(10)) return 29
# print(prime_number(100)) return 541
# print(prime_number(1000)) return 7919
# print(prime_number(10001)) return 104743

# My current algorithm is super slow for test case 10001th prime number.
# There should be a room for improvement.