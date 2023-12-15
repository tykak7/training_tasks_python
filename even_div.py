# The number 2520 is the smallest number that is 
# divisible by all numbers from 1 to 10. 
#Find the smallest positive number that is divisible without remainder by all numbers from 1 to 30.

import math # enter the library

c = math.lcm(*range(1, 31)) # Find the LCM (least common multiple) for numbers from 1 to 30

print(c)
