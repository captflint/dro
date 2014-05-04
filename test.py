# (C) 2014 James Stephenson

from marc import readmarc, parsesf, MARCrecord
from taglookup import gettag, getsubtag

testrecord = MARCrecord()

marcfile = input('Name of file: ')
with open(marcfile, 'rt') as infile:
    testrecord.raw_marc21 = infile.read()

testrecord.build_tag_dict()
print(testrecord.tag_dict)
