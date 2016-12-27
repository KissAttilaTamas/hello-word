import os
import sys
import curses
FILENAME = "README.md"
FOLDER = "$HOME//hello-word/"
print('Read/Write the file (',FILENAME,')?')
v=input("r/w?")
if v=='r' or v=='R':
    r = open(os.path.expandvars(FOLDER+FILENAME), 'r')
    print( r.read())
    r.close()
elif v=='w' or v=='W':
    w = open(os.path.expandvars(FOLDER+FILENAME), 'a')
    while 1:
        try:
            txt=sys.stdin.readline()
            w.write(txt)
        except KeyboardInterrupt:
            break
        if not txt:
            break
    w.close()
