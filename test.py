# (C) 2014 James Stephenson

from marc import MARCrecord
from taglookup import gettag, getsubtag

testrecord = MARCrecord()

marcfile = input('Name of file: ')
with open(marcfile, 'rt') as infile:
    testrecord.raw_marc21 = infile.read()

testrecord.parse_marc21()
testrecord.display()


