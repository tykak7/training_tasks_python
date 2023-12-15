##Určete součet všech násobků 3 a 5 menších než 1234.
##EDIT 26.9.: Vzhledem k několika komentářům raději reformuluji zadání:
##Určete součet všech čísel, jež jsou násobkem 3 nebo 5 a jsou menší než 1234.

result = 0

for i in range(1234):
    if not i%3 or not i%5: 
        result = result + i

    
print("This is the result: ", result, "\n")
