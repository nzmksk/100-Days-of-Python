# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will
# be 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in Fibonacci sequence whose values do not exceed n, find the sum of the even-valued terms.

def sum_even_fibonacci(n):
    # This function returns the value of the nth term of the Fibonacci sequence
    def fibonacci(nth_term):
        if nth_term == 1:
            fibonacci_number = 1
        elif nth_term == 2:
            fibonacci_number = 2
        else:
            # Apply recursion technique
            fibonacci_number = fibonacci(
                nth_term - 2) + fibonacci(nth_term - 1)
        return fibonacci_number
    # This function returns the nth term of the Fibonacci sequence that exceeds the value of n

    def find_term():
        for i in range(1, n):
            if fibonacci(i) > n:
                return i
    # Map the range into the defined fibonacci function
    fibonacci_sequence = list(map(fibonacci, range(1, find_term())))
    sum = 0
    for x in fibonacci_sequence:
        if x % 2 == 0:
            sum += x
    return sum
