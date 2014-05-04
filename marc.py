# (C) 2014 James Stephenson

# readmarc() takes a MARC21 utf-8 record as a single string and
# returns a list of tuples where each tuple is is a tag and its
# corresponding field entry.
def readmarc(record):
    baseaddr = int(record[12:17])
    fields = []
    current = 24
    while record[current] != "":
        tag = record[current:current + 3]
        length = int(record[current + 3:current + 7])
        start = int(record[current + 7:current + 12])
        entry = record[baseaddr + start:baseaddr + start + length]
        fields.append((tag, entry))
        current = current + 12
    return(fields)

# parsesf() takes a field string and return a list of tuples where each
# tuple has two elements, the first is the subfield tag, the second is
# the subfield data
def parsesf(field):
    subfields = []
    current = 0
    subdata = ""
    while field[current] != '':
        current = current + 1
    while field[current] != "":
        if field[current] == "":
            subtag = field[current + 1]
            current = current + 1
        else:
            subdata = subdata + field[current]
        if field[current + 1] == "" or field[current + 1] == "":
            subfields.append((subtag, subdata))
            subdata = ""
            current = current + 1
        else:
            current = current + 1
    return(subfields)

class MARCrecord:
    raw_marc21 = "This is a string containing the raw MARC data"

#The tag dict contains marc tags as keys and field strings as values
    tag_dict = {}

    def build_tag_dict(self):
        baseaddr = int(self.raw_marc21[12:17])
        fields = []
        current = 24
        while self.raw_marc21[current] != "":
            tag = self.raw_marc21[current:current + 3]
            length = int(self.raw_marc21[current + 3:current + 7])
            start = int(self.raw_marc21[current + 7:current + 12])
            entry = self.raw_marc21[baseaddr + start:baseaddr + start + length]
            self.tag_dict[tag] = entry
            current = current + 12

