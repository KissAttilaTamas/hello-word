# 10.37. Hozzunk létre egy A listát, ami tartalmaz néhány elemet.
# Hozzuk létre ennek egy valódi másolatát az új B változóban.
# Ötlet : először hozzunk létre egy csupa nullákat tartalmazó B listát,
# aminek a mérete megegyezik az A lista méretével.
# Ezután helyettesítsük a nullákat az A elemeivel.

indul=[12,32,32,63,77,56,23,87]
veges=[0]*len(indul)
print(veges,'innen kezd')
x=0
for item in indul:
    veges[x]=item
    x=x+1
print (veges)    
    
