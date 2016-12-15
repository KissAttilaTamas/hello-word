import struct
import os
import sys
import curses
import zipfile
import datetime
FILENAME = "smcfancontrol_2_4.zip"
FOLDER = "$HOME//hello-word/"
#data = open(os.path.expandvars(FOLDER+FILENAME), 'rb').read()
# data = open('fajlom.zip', 'rb').read()
start = 0

def print_info(archive_name):
    zf = zipfile.ZipFile(archive_name)
    for info in zf.infolist():
        print (info.filename)
        print ('\tComment:\t', info.comment)
        print ('\tModified:\t', datetime.datetime(*info.date_time))
        print ('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
        print ('\tZIP version:\t', info.create_version)
        print ('\tCompressed:\t', info.compress_size, 'bytes')
        print ('\tUncompressed:\t', info.file_size, 'bytes')
        

print_info(os.path.expandvars(FOLDER+FILENAME))


xf = zipfile.ZipFile('zipfile_write_arcname.zip', mode='w')
try:
    xf.write('README.md', arcname='NOT_README.txt')
finally:
    xf.close()
print_info('zipfile_write_arcname.zip')
