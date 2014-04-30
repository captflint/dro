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
    current = 2
    subdata = ""
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

tagdict = {
'001': 'Control Number',
'003': 'Control Number Identifier',
'005': 'Date and Time of Latest Transaction',
'006': 'Fixed-Length Data Elements-Additional Material Characteristics',
'007': 'Physical Description Fixed Field-General Information',
'008': 'Fixed-Length Data Elements-Gerneral Information',
'010': 'Library of Congress Control Number',
'010a': 'LC control number',
'010b': 'NUCMC control number',
'010z': 'Canceled/invalid LC control number',
'0108': 'Field link and sequence number',
'013': 'Patent Control Information',
'013a': 'Number',
'013b': 'Country',
'013c': 'Type of number',
'013d': 'Date',
'013e': 'Status',
'013f': 'Party to document',
'0136': 'Linkage',
'0138': 'Field link and sequence number',
'015': 'National Bibliography Number',
'015a': 'National bibliography number',
'015q': 'Qualifying information',
'015z': 'Canceled/invalid national bibliography number',
'0152': 'Source',
'0156': 'Linkage',
'0158': 'Field link and sequence number',
'016': 'National Bibliographic Agency Control Number',
'016a': 'Record control number',
'016z': 'Canceled/invalid control number',
'0162': 'Source',
'0168': 'Field link and sequence number',
'017': 'Copyright or Legal Deposit Number',
'017a': 'Copyright or legal deposit number',
'017b': 'Assigning agency',
'017d': 'Date',
'017i': 'Display text',
'017z': 'Canceled/invalid copyright or legal deposit number',
'0172': 'Source',
'0176': 'Linkage',
'0178': 'Field link and sequence number',
'018': 'Copyright Article-Fee Code',
'018a': 'Copyright article-fee code',
'0186': 'Linkage',
'0188': 'Field link and sequence number',
'020': 'International Standard Book Number',
'020a': 'ISBN',
'020c': 'Terms of availability',
'020q': 'Qualifying information',
'020z': 'Canceled/invalid ISBN',
'0206': 'Linkage',
'0208': 'Field link and sequence number',
'022': 'International Standard Serial Number',
'022a': 'ISSN',
'022l': 'ISSN-L',
'022m': 'Canceled ISSN-L',
'022y': 'Incorrect ISSN',
'022z': 'Canceled ISSN',
'0222': 'Source',
'0226': 'Linkage',
'0228': 'Field link and sequence number',
'024': 'Other Standard Identifier',
'024a': 'Standard number or code',
'024c': 'Terms of availability',
'024d': 'Additional codes following the standard number or code',
'024q': 'Qualifying information',
'024z': 'Canceled/invalid standard number or code',
'0242': 'Source of number or code',
'0246': 'Linkage',
'0248': 'Field link and sequence number',
'025': 'Overseas Acquisition Number',
'025a': 'Overseas acquisition number',
'0258': 'Field link and sequence number',
'026': 'Fingerprint Identifier',
'026a': 'First and second groups of characters',
'026b': 'Third and fourth groups of characters',
'026c': 'Date',
'026d': 'Number of volume or part',
'026e': 'Unparsed fingerprint',
'0262': 'Source',
'0265': 'Institution to which field applies',
'0266': 'Linkage',
'0268': 'Field link and sequence number',
'027': 'Standard Technical Report Number',
'027a': 'Standard technical report number',
'027q': 'Qualifying information',
'027z': 'Canceled/invalid number',
'0276': 'Linkage',
'0278': 'Field link and sequence number',
'028': 'Publisher Number',
'028a': 'Publisher number',
'028b': 'Source',
'028q': 'Qualifying information',
'0286': 'Linkage',
'0288': 'Field link and sequence number',
'030': 'CODEN Designation',
'030a': 'CODEN',
'030z': 'Canceled/invalid CODEN',
'0306': 'Linkage',
'0308': 'Field link and sequence number',
'031': 'Musical Incipits Information',
'031a': 'Number of work',
'031b': 'Number of movement',
'031c': 'Number of excerpt',
'031d': 'Caption or heading',
'031e': 'Role',
'031g': 'Clef',
'031m': 'Voice/instrument',
'031n': 'Key signature',
'031o': 'Time signature',
'031p': 'Musical notation',
'031q': 'General note',
'031r': 'Key or mode',
'031s': 'Coded validity note',
'031t': 'Text incipit',
'031u': 'Uniform Resource Identifier',
'031y': 'Link text',
'031z': 'Public note',
'0312': 'System code',
'0316': 'Linkage',
'0318': 'Field link and sequence number',
'
}

