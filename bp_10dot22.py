# 10.22. Írjon egy scriptet, ami egy szövegfileban megszámolja a szavakat.

import os
import sys
import curses
FILENAME = "README.md"
FOLDER = "$HOME//hello-word/"
egyik = open(os.path.expandvars(FOLDER+FILENAME), 'r')
x=1
szavak=0
e='jjjj'
while len(e)>0:
    try:
        e=egyik.readline()
        f=e.split()
        k=len(f)
    except EOFError:
        break
    szavak=szavak+k
    print(e,f,k,x,szavak)
    x=x+1

print(x,' sor olvasva es ',szavak, ' szo volt bennuk')
print (e,'\n',f,k)
egyik.close()

