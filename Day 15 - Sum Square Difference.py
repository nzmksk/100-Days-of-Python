# The sum of the squares of the first ten natural numbers is 1**2 + 2**2 + ... + 10**2 = 385
# The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)**2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.

def sum_square_difference(n):
    def sum_of_square():
        sum = 0
        for i in range(1, n + 1):
            sum += i**2
        return sum

    def square_of_sum():
        squared = 0
        for i in range(1, n + 1):
            squared += i
        return squared**2

    return square_of_sum() - sum_of_square()
