import struct
import os
import sys
import curses
FILENAME = "smcfancontrol_2_4.zip"
FOLDER = "$HOME//hello-word/"
data = open(os.path.expandvars(FOLDER+FILENAME), 'rb').read()
# data = open('fajlom.zip', 'rb').read()
start = 0
for i in range(3):                      # megnezzuk az elso harom fajl fejlecet
    start += 14
    fields = struct.unpack('LLLHH', data[start:start+28])
    crc32, comp_size, uncomp_size, filenamesize, extra_size =  fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # tovabblepes a kovetkezo fejlechez
