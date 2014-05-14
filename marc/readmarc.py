# (C) 2014 James Stephenson

import sys
from marc import MARCrecord
from preprocessmarc import separate

with open(sys.argv[1], 'rb') as infile:
    marcfile = infile.read()

test = MARCrecord()
test.raw_marc21 = marcfile
test.parse_marc21()
test.display()
test.buildrecord()
