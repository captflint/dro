# (C) 2014 James Stephenson

from decodemarc8 import convertmarc8

def newrecord(chars):
    for c in chars:
        if c not in bytes('1234567890', 'utf-8'):
            return(False)
    return(True)

def separate(records):
    returnlist = []
    recordstring = bytes('', 'utf8')
    recording = False
    while len(records) > 0:
        while recording:
            if records[0] != int('0x1d', base = 16):
                recordstring += bytes([records[0]])
                records = records[1:]
            else:
                recordstring += bytes([records[0]])
                records = records[1:]
                if recordstring[9] != ord('a'):
                    recordstring = convertmarc8(recordstring)
                else:
                    recordstring = bytes.decode(recordstring, 'utf-8')
                returnlist.append(recordstring)
                recordstring = ''
                recording = False
        if newrecord(records[0:5]):
            recording = True
        else:
            records = records[1:]
    return(returnlist)
