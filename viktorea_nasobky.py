# Consider natural numbers less than 10 that are multiples
# of 3 or 5 (i.e. 3; 5; 6; 9). The sum of these multiples is 23.

# Determine the sum of all multiples of 3 and 5 less than 1234.

result = 0

for i in range(1234):
    if not i%3 or not i%5: 
        result = result + i

    
print("This is the result: ", result, "\n")
