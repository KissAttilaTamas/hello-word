# 10.40. Egy primszám olyan szám, ami csak eggyel és önmagával osztható.
# Írjon programot, ami az eratosztenészi szita módszerének alkalmazásával


sor=range(1000)
indeksz=[1]
indeksz=indeksz*1000
x=2
y=2
# print(sor, indeksz) 
while x<sor[999]:
    while x*y<sor[999]:
        indeksz[x*y]=0
        # print(x,y,x*y, indeksz[x*y])
        y=y+1
    x=x+1
    y=2
print(indeksz)    
    
z=2
while z<sor[999]:
        if indeksz[z]==1:
            print(z," egy primszam")
        else:
            pass
        z=z+1
        
