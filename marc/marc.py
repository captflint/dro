# (C) 2014 James Stephenson
from taglookup import getsubtag, gettag
from decodemarc8 import convertmarc8

class MARCrecord:
    def __init__(self):
        self.raw_marc21 = 'Raw MARC21 data goes here'

# record is a list of many sublists with tags and data
        self.record = []
        self.leader = Leader()
        self.ismarc8 = False
        self.newrecord = []
        self.fieldstring = ""

    def unicodec(self, bites):
        if self.ismarc8:
            return(convertmarc8(bites))
        else:
            return(bytes.decode(bites, 'utf-8'))
        
# parse_marc21 takes a raw MARC 21 file encoded in utf8
# and proceses it so it can be manipulated by the program
    def parse_marc21(self):
# The first step in the process is to parse the directory
        rawmarc = self.raw_marc21
        self.leader.parse(rawmarc[:24])
        if self.leader.encoding != 'a':
            self.ismarc8 = True
        baseaddr = int(self.leader.base_addr)
        current = 24
        while chr(rawmarc[current]) != "":
            tag = rawmarc[current:current + 3]
            length = int(rawmarc[current + 3:current + 7])
            start = int(rawmarc[current + 7:current + 12])
            entry = rawmarc[baseaddr + start:baseaddr + start + length]
            self.record.append([bytes.decode(tag), self.unicodec(entry)])
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
        print("Leader")
        print(self.leader.whole_leader, '\n')
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

    def buildrecord(self):
        sortlist = []
        for dexnum in range(0, len(self.record)):
            sortlist.append((self.record[dexnum][0], dexnum))
        sortlist.sort()
        for f in sortlist:
            self.newrecord.append(self.record[f[1]])
        for l in self.newrecord:
            del l[0]
        for x in range(0, len(self.newrecord)):
            self.newrecord[x] = self.newrecord[x][0]
        for item in range(0, len(self.newrecord)):
            if type(self.newrecord[item]) is list:
                for x in range(1, len(self.newrecord[item])):
                    self.newrecord[item][x][0] = '' + self.newrecord[item][x][0]
                self.newrecord[item][-1][1] += ''
            else:
                self.newrecord[item] += ''
        fields = self.stringifylist(self.newrecord) + ''
        current = 0
        start = 0
        direc = ""
        for tagtup in sortlist:
            tag = tagtup[0]
            length = 1
            while fields[current] != '':
                length += 1
                current += 1
            length += 1
            current += 1
            lendiff = 4 - len(str(length))
            startdiff = 5 - len(str(start))
            direc += tag + ('0' * lendiff + str(length)) + ('0' * startdiff + str(start))
            start += length + 1
        direc += ''
        self.leader.encoding = 'a'
        totallength = 24 + len(direc) + len(fields)
        totallength = (5 - len(str(totallength))) * '0' + str(totallength)
        self.leader.record_length = totallength
        ba = 24 + len(direc)
        self.leader.base_addr = (5 - len(str(ba))) * '0' + str(ba)
        self.leader.build()
        self.raw_marc21 = self.leader.whole_leader + direc + fields

    def stringifylist(self, tsil):
        returnstring = ""
        for x in range(0, len(tsil)):
            if type(tsil[x]) is str:
                returnstring += tsil[x]
            elif type(tsil[x]) is list:
                returnstring += self.stringifylist(tsil[x])
            else:
                return("stringify error")
        return(returnstring)

class Leader():
    def __init__(self):
        self.whole_leader = "The whole leader goes here"
        self.record_length = "Marc record length goes here"
        self.record_status = "Marc record status goes here"
        self.record_type = "Type of record goes here"
        self.bib_level = "Bibliographic level goes here"
        self.control_type = "Type of control goes here"
        self.encoding = "Character encoding scheme goes here"
        self.indicator_count = '2' #This value never changes
        self.sub_code_count = '2' #This value never changes
        self.base_addr = "Base address of data goes here"
        self.encoding_level = "Encoding level goes here"
        self.descriptive_cataloging = "Descriptive cataloging form goes here"
        self.multipart_record_level = "Multipart Resourse Record Level goes here"
        self.length_of_length = '4' #This value never changes
        self.length_of_start = '5' #This value never changes
        self.length_of_implementation = '0' #This value never changes
        self.undefined = '0' #This value never changes

    def parse(self, raw_leader):
        if type(raw_leader) != str:
            raw_leader = bytes.decode(raw_leader)
        self.whole_leader = raw_leader
        self.record_length = raw_leader[0:5]
        self.record_status = raw_leader[5]
        self.record_type = raw_leader[6]
        self.bib_level = raw_leader[7]
        self.control_type = raw_leader[8]
        self.encoding = raw_leader[9]
        self.base_addr = raw_leader[12:17]
        self.encoding_level = raw_leader[17]
        self.descriptive_cataloging = raw_leader[18]
        self.multipart_record_level = raw_leader[19]

    def build(self):
        self.whole_leader = self.record_length
        self.whole_leader += self.record_status
        self.whole_leader += self.record_type
        self.whole_leader += self.bib_level
        self.whole_leader += self.control_type
        self.whole_leader += self.encoding
        self.whole_leader += self.indicator_count
        self.whole_leader += self.sub_code_count
        self.whole_leader += self.base_addr
        self.whole_leader += self.encoding_level
        self.whole_leader += self.descriptive_cataloging
        self.whole_leader += self.multipart_record_level
        self.whole_leader += self.length_of_length
        self.whole_leader += self.length_of_start
        self.whole_leader += self.length_of_implementation
        self.whole_leader += self.undefined
