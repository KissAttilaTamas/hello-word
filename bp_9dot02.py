import os
import sys
import curses
FILENAME = "README.md"
FOLDER = "$HOME//hello-word/"
f1=input('File comparison \n Please give me the first file name:')
f2=input('Please give me the second file name:')
egyik = open(os.path.expandvars(FOLDER+f1), 'r')
masik = open(os.path.expandvars(FOLDER+f2), 'r')
x=0
hiba=0
e='jjjj'
while hiba==0 and len(e)>0:
    try:
        e=egyik.readline()
        m=masik.readline()
        print(e,m,x)
        if e==m:
            x=x+1
        else:
            hiba=1
            x=x+1
            break
    except EOFError:
        break
print(x+1,' sor olvasva es ',hiba,' hiba')
print (e,'\n',m)
egyik.close()
masik.close()
