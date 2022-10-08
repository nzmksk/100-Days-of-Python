# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two n-digit numbers.

def largest_palindrome(n):
    def interval(n):
        return range(10**(n-1), 10**n)

    largest_palindrome = None
    for i in interval(n):
        for j in interval(n):
            product = i * j
            if str(product) == str(product)[::-1]:
                if largest_palindrome == None or largest_palindrome < product:
                    largest_palindrome = product

    return largest_palindrome

# Current algorithm is tediously slow starting n = 4.
# Definitely there's a room for improvement to make the algorithm faster.
