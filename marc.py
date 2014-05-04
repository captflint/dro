# (C) 2014 James Stephenson
from taglookup import getsubtag, gettag

class MARCrecord:
    raw_marc21 = "This is a string containing the raw MARC data"

#The tag dict contains marc tags as keys and field strings as values
    record = []

    def parse_marc21(self):
        baseaddr = int(self.raw_marc21[12:17])
        current = 24
        while self.raw_marc21[current] != "":
            tag = self.raw_marc21[current:current + 3]
            length = int(self.raw_marc21[current + 3:current + 7])
            start = int(self.raw_marc21[current + 7:current + 12])
            entry = self.raw_marc21[baseaddr + start:baseaddr + start + length]
            self.record.append([tag, entry])
            current = current + 12
        for x in range(0, len(self.record)):
            if '' not in self.record[x][1]:
                self.record[x][1] = self.record[x][1][:-1]
            else:
                fieldstring = self.record[x][1][:-1]
                fielddata = []
                if '' in fieldstring[:2]:
                    fielddata.append('invalid indicators')
                else:
                    fielddata.append(fieldstring[:2])
                while fieldstring[0] != '':
                    fieldstring = fieldstring[1:]
                fieldstring = fieldstring[1:]
                choplist = []
                chopstr = ''
                for char in fieldstring:
                    if char != '':
                        chopstr = chopstr + char
                    else:
                        choplist.append(chopstr)
                        chopstr = ''
                choplist.append(chopstr)
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
