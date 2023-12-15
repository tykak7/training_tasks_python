#Číslo 2520 je nejmenší číslo které je dělitelné bezezbytku všemi číslo od 1 do 10.
#Nalezněte nejmenší kladné číslo,
#které je dělitelné bezezbytku všemi čísly od 1 do 30.
# Řešení: 2329089562800

import math # enter the library

c = math.lcm(*range(1, 31)) # Find the LCM (least common multiple) for numbers from 1 to 30

print(c)
