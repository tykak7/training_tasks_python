
def fibonacci(minus_prvni, minus_druhi):
    result = minus_prvni + minus_druhi
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
