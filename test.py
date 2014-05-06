# (C) 2014 James Stephenson

import sys
from marc import MARCrecord
from preprocessmarc import separate

with open(sys.argv[1], 'rt') as infile:
    marcfile = separate(infile.read())

objectlist = []
for item in marcfile:
    x = MARCrecord()
    x.raw_marc21 = item
    objectlist.append(x)
    x = "I'm not an object anymore"

for obj in objectlist:
    obj.parse_marc21()
    print('\n NEWNEWNEW \n')
    obj.display()
