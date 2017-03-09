# Van egy numerikus értékeket tartalmazó file. Tegyük fel, hogy ezek az értékek
# egy gömbsorozat átmérői. Írjon egy scriptet, ami arra használja föl ennek
# a file­nak az adatait, hogy egy másik szövegsorokba rendezett filet hoz létre,
# ami ezeknek a gömböknek más jellemzőit fejezi ki (főkör területe, felület,
# térfogat) a következő formában :
# d 46.20 cm Ft = 1676.39 cm2 Fel. = 6705.54 cm2. Tf. = 51632.67 cm3
# d. 120.00 cm Ft = 11309.73 cm2 Fel. = 45238.93 cm2. Tf. = 904778.68 cm3
# d. 0.03cmFt= 0.00cm2Fel.= 0.00cm2.Tf.= 0.00cm3 d. 13.90 cm Ft = 151.75 cm2
# d. 88.80 cm FT = 6193.21 cm2 Fel. = 24772.84 cm2. Tf. = 366638.04 cm3
# stb.

import os
import sys
import curses
import math
FILENAME = "KOR.txt"
FILENAME2 = "KOROK.txt"
FOLDER = "$HOME//hello-word/"
olvas= open(os.path.expandvars(FOLDER+FILENAME), 'r')
kiir = open(os.path.expandvars(FOLDER+FILENAME2), 'w')
x=1
e='jjjj'
while len(e)>0:
    try:
        e=olvas.readline()
        if len(e)>0:
            r=float(e)
            k=kiir.write("kor sugara = %.2f cm  felszin = %.2f cm2 terfogat= %.2f cm3" % (r,4*r**2*math.pi,(4*r**3*math.pi)/3)+"\n")
            print(x,r,4*r**2*math.pi,(4*r**3*math.pi)/3)
        else:
             pass
    except EOFError:
        break
    x=x+1
olvas.close()
kiir.close()

