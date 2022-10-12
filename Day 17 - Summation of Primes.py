# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all primes below n.

def prime_summation(n):
    sum = 2
    if n == 2:
        return sum
    elif n < 2:
        return None
    else:
        for odd_num in range(3, n, 2):
            for i in range(3, odd_num, 2):
                if odd_num % i == 0:
                    break
            else:
                sum += odd_num
        return sum

# TEST CASES
# print(prime_summation(17)) returns 41
# print(prime_summation(2001)) returns 277050
# print(prime_summation(140759)) returns 873608362
# print(prime_summation(2000000)) returns 142913828922

# My algorithm only viable for test case 1 and 2.
# For test case 3 and 4, the number is too large to process, so there might be a faster solution.