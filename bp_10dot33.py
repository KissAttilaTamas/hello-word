# 10.33. Írjon egy scriptet, ami kiíratja egy csütörtöki nappal kezdődő
# képzeletbeli év napjainak a listáját.


honap=['Januar','Februar','Marcius','Aprilis','Majus','Junius','Julius','Augusztus','Szeptember','Oktober','November','December']
hnapok=[31,28,31,30,31,30,31,31,30,31,30,31]
napok=['Csutortok','Pentek','Szombat','Vasarnap','Hetfo','Kedd','Szerda']

x=0
s=1
while x<12:
    y=1
    while y<hnapok[x]+1:
        print(x+1,honap[x],y,napok[(y-1)%7])
        y=y+1  
    x=x+1
pass    
