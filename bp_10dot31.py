# 10.31. Van egy egész számokat tartalmazó lista, amiben egyes számok többször
# is előfordulnak. Írjon egy scriptet, ami a listát úgy másolja át egy másik
# listába, hogy figyelmen kívül hagyja a többszöri előfordulásokat.
# A végső listának rendezettnek kell lenni.

def maxlista(listf):
    listf.sort()
    s=len(listf)-1
    return listf[s]

lista=[1,34,45,67,54,32,3,55,167,34,55,12,3,4,90]
newl=[-999]
x=0
lista.sort()
while x<len(lista)-1:
    if lista[x]>maxlista(newl):
        newl.append(lista[x])
    else:
        pass
    x=x+1
del newl[0]
print(lista, newl)    
    
