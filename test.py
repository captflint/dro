# (C) 2014 James Stephenson

import sys
from marc import MARCrecord
from preprocessmarc import separate

with open(sys.argv[1], 'rt') as infile:
    marcfile = separate(infile.read())

one = MARCrecord()
two = MARCrecord()
three = MARCrecord()
four = MARCrecord()
five = MARCrecord()

one.raw_marc21 = marcfile[0]
two.raw_marc21 = marcfile[1]
three.raw_marc21 = marcfile[2]
four.raw_marc21 = marcfile[3]
five.raw_marc21 = marcfile[4]

one.parse_marc21()
two.parse_marc21()
three.parse_marc21()
four.parse_marc21()
five.parse_marc21()

print('\n NEWNEWNEW \n')
print(one.record)
print('\n NEWNEWNEW \n')
print(two.record)
print('\n NEWNEWNEW \n')
print(three.record)
print('\n NEWNEWNEW \n')
print(four.record)
print('\n NEWNEWNEW \n')
print(five.record)

