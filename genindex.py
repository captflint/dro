# (C) 2014 James Stephenson

#This file gererates an index from a list of MARC data
#provided by The Library of Congress.  If that list is
#modified, the index has to be regenerated.

with open('MARC21bibfieldlist.txt', 'rt') as infile:
    marcdata = infile.read()

def stringify(tag):
    if tag < 10:
        return('00' + str(tag))
    elif tag < 100:
        return('0' + str(tag))
    else:
        return(str(tag))

index = {}
tag = 0
while tag < 1000:
    current = 0
    search = stringify(tag) + ' - '
    print("Searching for", search[:3])
    while marcdata[current:current + 6] != search and marcdata[current:current + 10] != '!!!!!!!!!!':
        current = current + 1
    if marcdata[current:current + 6] == search:
        print(search[:3], 'is at', current)
        index[search[:3]] = current
    else:
        print(search[:3], 'not found')
    tag = tag + 1
print(index)
