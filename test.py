# (C) 2014 James Stephenson

from marc import MARCrecord
from taglookup import gettag, getsubtag

testrecord = MARCrecord()

marcfile = input('Name of file: ')
with open(marcfile, 'rt') as infile:
    testrecord.raw_marc21 = infile.read()

testrecord.parse_marc21()
for item in testrecord.record:
    print(item[0])
    if type(item[1]) is list:
        for x in item[1]:
            print(x)
    else:
        print(item[1])

print(testrecord.record)

