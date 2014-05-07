# (C) 2014 James Stephenson
from taglookup import getsubtag, gettag

class MARCrecord:
    def __init__(self):
        self.raw_marc21 = 'Raw MARC21 data goes here'

# record is a list of many sublists with tags and data
        self.record = []

# parse_marc21 takes a raw MARC 21 file encoded in utf8
# and proceses it so it can be manipulated by the program
    def parse_marc21(self):
# First we get the raw data and add some padding
        rawmarc = bytes(self.raw_marc21, 'utf-8')
# The first step in the process is to parse the directory
        baseaddr = int(rawmarc[12:17])
        current = 24
        while chr(rawmarc[current]) != "":
            tag = rawmarc[current:current + 3]
            length = int(rawmarc[current + 3:current + 7])
            start = int(rawmarc[current + 7:current + 12])
            entry = rawmarc[baseaddr + start:baseaddr + start + length]
            self.record.append([bytes.decode(tag), bytes.decode(entry)])
            current += 12

# At this point the directory has been parsed and the
# tags and data have been stored is a list of lists.
# ==== List data structure ====
# 1st Level:
# Each item is a list with two items. The first item
# is the field tag. The 2nd is the field data. Fields
# with no subfields stay on this level.
# 2nd Level:
# The data from level 1 gets turned from a string into
# a list. The first item are the indicators. The next
# items are 3rd level sublists.
# 3rd level:
# Each 3rd level sublist has two items. The 1st is
# the subfield tag. The 2nd is the subfield data
        for x in range(0, len(self.record)):
# Check to see if the data field has subfields, if not
# knock off the final character which we don't need.
            if '' not in self.record[x][1]:
                self.record[x][1] = self.record[x][1][:-1]
            else:
                fieldstring = self.record[x][1][:-1]
                fielddata = []
# Check for valid indicators and add them to the list
                if '' in fieldstring[:2]:
                    fielddata.append('invalid indicators')
                else:
                    fielddata.append(fieldstring[:2])
# Skip to the beginning of the first subfield
                while fieldstring[0] != '':
                    fieldstring = fieldstring[1:]
                fieldstring = fieldstring[1:]

# Now we chop the field data string into separate
# subfield strings
                choplist = []
                chopstr = ''
                for char in fieldstring:
                    if char != '':
                        chopstr = chopstr + char
                    else:
                        choplist.append(chopstr)
                        chopstr = ''
                choplist.append(chopstr)

# separate each subtag from its subdata, put it
# in a list and add everything to the record.
                for item in choplist:
                    fielddata.append([item[0], item[1:]])
                self.record[x][1] = fielddata

    def display(self):
        for item in self.record:
            print(gettag(item[0]))
            if type(item[1]) is str:
                print('\t', item[1], '\n')
            else:
                for sub in item[1]:
                    if type(sub) is str:
                        print(sub)
                    else:
                        print('\t', getsubtag(item[0], sub[0]))
                        print('\t\t', sub[1], '\n')

