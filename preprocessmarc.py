def newrecord(chars):
    for c in chars:
        if c not in '1234567890':
            return(False)
    return(True)

def separate(records):
    returnlist = []
    recordstring = ''
    recording = False
    while len(records) > 0:
        while recording:
            if records[0] != '':
                recordstring += records[0]
                records = records[1:]
            else:
                recordstring += records[0]
                records = records[1:]
                returnlist.append(recordstring)
                recordstring = ''
                recording = False
        if newrecord(records[0:5]):
            recording = True
        else:
            records = records[1:]
    return(returnlist)
