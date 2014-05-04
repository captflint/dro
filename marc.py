# (C) 2014 James Stephenson
from taglookup import getsubtag, gettag

class MARCrecord:
    raw_marc21 = "This is a string containing the raw MARC data"

#The tag dict contains marc tags as keys and field strings as values
    record = []

    def parse_marc21(self):
        self.raw_marc21 = self.raw_marc21 + '!!!!!!!!!!!!!!!'
        baseaddr = int(self.raw_marc21[12:17])
        current = 24
        offset = 0
        newoffset = False
        olderoffset = 0
        while self.raw_marc21[current] != "":
            tag = self.raw_marc21[current:current + 3]
            length = int(self.raw_marc21[current + 3:current + 7])
            start = int(self.raw_marc21[current + 7:current + 12])
            if self.raw_marc21[baseaddr + start + length + offset - 1] != '':
                olderoffset = offset
                offset = 0
                oldoffset = 0
                newoffset = True
                while self.raw_marc21[baseaddr + start + length + offset - 1] != '':
                    if offset == oldoffset * -1:
                        oldoffset = offset
                        if offset < 0:
                            offset = offset * -1
                        offset = offset + 1
                    else:
                        oldoffset = offset
                        offset = offset * -1
            print('offset is', offset)
            if newoffset is False:
                entry = self.raw_marc21[baseaddr + start + offset:baseaddr + start + length + offset]
            else:
                entry = self.raw_marc21[baseaddr + start + olderoffset:baseaddr + start + length + offset]
                newoffset = False
            print(tag, entry)
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
