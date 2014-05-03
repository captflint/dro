# (C) 2014 James Stephenson

from marc import readmarc, parsesf
from taglookup import gettag, getsubtag
marcfile = input('Name of file: ')
with open(marcfile, 'rt') as infile:
    marcfile = infile.read()

for field in readmarc(marcfile):
    print(gettag(field[0]))
    if '' in field[1]:
        for sub in parsesf(field[1]):
            print('\t', getsubtag(field[0], sub[0]))
            print('\t\t', sub[1])
    else:
        print('\t', field[1][:-1])
    print('\n')
