import os
import sys
import curses
FILENAME = "README.md"
FOLDER = "$HOME//hello-word/"
f1=input('File comparison \n Please give me the first file name:')
f2=input('Please give me the second file name:')
egyik = open(os.path.expandvars(FOLDER+FILENAME), 'r')
x=1
hiba=0
e='jjjj'
while len(e)>0:
    try:
        e=egyik.readline()
        print(x,len(e),"*"+e+"*")
        x=x+1
    except EOFError:
        break
print(x,' sor olvasva es ',hiba,' hiba')
egyik.close()

