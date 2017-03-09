# 10.41. Írja újra a fenti veletlen_lista() függvényt az append() metódus alkalmazásával úgy,
# hogy a listát egy üres listából lépésről-lépésre hozza létre (azaz ne egy már meglévő lista nulla

import random
import scikit-learn

def veletlen_lista(n):
    s = [0]*n
    for i in range(n):
        s[i] = random.randint(0,100)
    return s

def veletlen_lista2(n):
    z=1
    lista=[]
    while z<n:
        lista.append(random.randint(0,100))
        z=z+1
    return lista


print(veletlen_lista2(100))
