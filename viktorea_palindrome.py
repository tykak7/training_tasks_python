#Nalezněte nevětší palindromické číslo které je součinem dvou 4 místných čísel.
#Řešení: 99000099

# Checks if a number is a palindrome (číslo, které je v obou směrech stejné)
def is_palindrome(num): #(argument) parentheses are mandatory!!
    num_str = str(num) #convert the number to a string
    # returns TRUE if YES - they are equal
    return num_str == num_str[::-1] # num_str compared to its inverted version.

def largest_palindrome_product():
    max_palindrome = 0


    # Enumeration of all possible four-digit numbers
    for i in range(9999, 999, -1):
#First argument (start): 9999 in this case is the start value of the range. The loop will start from this value.

#Second argument (stop): 999 in this case is the end value of the range
#(not inclusive). The loop will continue as long as the variable i is greater than this value.

# Third argument (step): -1 in this case indicates the step at which the #values of variable i will change
# values of variable i.
#In this case, a step of -1 means that the variable i will be decremented by 1 at each # iteration of the loop.
#iteration of the loop.
        
        for j in range(i, 999, -1):
            product = i * j


            if product <= max_palindrome:
                # If the product is already less than or equal to the maximal palindrome, exit the loop
                break

            if is_palindrome(product):
                max_palindrome = product

    return max_palindrome

# Find the largest palindromic product
result = largest_palindrome_product()
print("Největší palindromické číslo které je součinem dvou 4 místných čísel:", result)
