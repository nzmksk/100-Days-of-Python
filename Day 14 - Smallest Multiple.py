# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all numbers from 1 to n?

def smallest_multiple(n):
    # Common multiple of the two highest natural numbers
    num = n * (n - 1)
    increment = num

    def find_multiple(num):
        while True:
            for i in range(n - 2, 1, -1):
                # If current multiple is not evenly divisible by i, increment the current multiple value
                if num % i != 0:
                    num += increment
                    # Break statement will restart the for loop from the first i
                    break
            # This line will only get executed if the if (within for loop) all return False for each iteration of i
            else:
                return num

    return find_multiple(num)
