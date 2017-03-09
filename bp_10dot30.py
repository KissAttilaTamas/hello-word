# 10.30. Legyen adott a következő lista :
# ['Jean­Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre­Benoît', 'Louise']
# Írjon egy scriptet, ami kiírja a neveket és a nevekben lévő karakterek számát.

x=0
koteg=['Jean­Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre­Benoît', 'Louise']
while x<len(koteg):
    print(str(x+1)+".k elem: ",koteg[x]," hossza: ",len(koteg[x]))
    x=x+1
    
