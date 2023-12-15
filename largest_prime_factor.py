# The prime factors of 13195 are 5, 7, 13 and 29.
# Find the greatest prime divisor of 70616204741131.

n = 70616204741131
p = 3 # checking the divisors

while p * p < n:
    if n % p == 0: # test for division without remainder
        n //= p # if it divides without remainder, the result is
        # division assigned to the variable n

    else:
        p += 2 # increase the divisor, odd number
   
print(n) 
