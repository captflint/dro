# (C) 2014 James Stephenson
from taglookup import getsubtag, gettag

class MARCrecord:
    raw_marc21 = "This is a string containing the raw MARC data"

# record is a list of many sublists with tags and data
    record = []

# parse_marc21 takes a raw MARC 21 file encoded in utf8
# and proceses it so it can be manipulated by the program
    def parse_marc21(self):
# First we get the raw data and add some padding
        rawmarc = self.raw_marc21 + 100 * '!'
# The first step in the process is to parse the directory
        baseaddr = int(rawmarc[12:17])
        current = 24
        offset = 0
        newoffset = False
        lastoffset = 0
        while rawmarc[current] != "":
            tag = rawmarc[current:current + 3]
            length = int(rawmarc[current + 3:current + 7])
            start = int(rawmarc[current + 7:current + 12])
# The following statements check for currupted directory
# data and try to compensate
            if rawmarc[baseaddr + start + length + offset - 1] != '':
                lastoffset = offset
                offset = 0
                oldoffset = 0
                newoffset = True
                while rawmarc[baseaddr + start + length + offset - 1] != '':
                    if offset == oldoffset * -1:
                        oldoffset = offset
                        if offset < 0:
                            offset = offset * -1
                        offset = offset + 1
                    else:
                        oldoffset = offset
                        offset = offset * -1

            #print('offset is', offset) # used for debugging
            if newoffset is False:
                entry = rawmarc[baseaddr + start + offset:baseaddr + start + length + offset]
            else:
                entry = rawmarc[baseaddr + start + lastoffset:baseaddr + start + length + offset]
                newoffset = False
            #print(tag, entry[-1]) #used for debugging
            self.record.append([tag, entry])
            current = current + 12

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
