def csakkicsi(sztring):
    x=0
    vissza=''
    while x<=len(sztring)-1:
        if 'A'<=sztring[x]<='Z':
            vissza=vissza+chr(ord(sztring[x])+32)
        else:
            vissza=vissza+sztring[x]
        x=x+1
    return vissza

print(csakkicsi('A Macsaka helyes AllatKA'))    
