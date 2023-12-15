n = 70616204741131
p = 3 # kontrolujeme dělitele

while p * p < n:
    if n % p == 0: # test pro dělení beze zbytku
        n //= p # pokud dělí beze zbytku, je výsledek
        # dělení přiřazen proměnné n

    else:
        p += 2 # zvětšíme dělitele, liché číslo
   
print(n) 
