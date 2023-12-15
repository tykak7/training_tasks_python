# Consider the members of the Fibonacci sequence
# whose value is not greater than 5,000,000. 
# Find the sum of the even terms in this part of the sequence.

def fibonacci(minus_first, minus_second):
    result = minus_first + minus_second
    return result

summ = 0        
n_two = 0
n_one = 1
n = 0

while n <= 5000000:
    if not n % 2:
        summ = summ + n
    n = fibonacci(n_one, n_two)
    n_two = n_one
    n_one = n

print("The end result: ", summ, "\n")
