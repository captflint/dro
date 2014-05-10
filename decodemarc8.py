# (C) 2014 - James Stephenson

from MARC8dicts import Ascii, Ansel, Greeksymbols, Subscripts, Superscripts, Basichebrew, Basiccyrillic, Extendedcyrillic, Basicarabic, Extendedarabic, Basicgreek, Asiadict

# Define some character set properties
charsetcodes = {'3': Basicarabic, '4': Extendedarabic, 'B': Ascii, '!E': Ansel, '1': Asiadicts, 'N': Basiccyrillic, 'Q': Extendedcyrillic, 'S': Basicgreek, '2': Basichebrew}

G0 = Ascii
G1 = Ansel


def convertmarc8(marcbytes):
    utfstring = bytes('')
    while len(marcbytes) > 0:
        if bite == bytes.(0x1b):
            changecharset(marcbytes)
        else:
            if GO == Ascii and ord(bite) <= 127:
                utfstring += bite
                marcbytes = marcbytes[1:]
            elif ord(bite) <= 127:
                utfstring += utfcodelookup(G0, bite)
                marcbytes = marcbytes[1:]
            else:
                utfstring += utfcodelookup(G1, bite)
                marcbytes = marcbytes[1:]
    return(cleanup(utfstring))

def cleanup(string):
#This function will put combining characters in the
#correct positions and return a utf-8 string

def changecharset(truncatedbytes):
#This will change the character set and return
#the bites minus the escape sequence
    global G0
    global G1
    truncatedbytes = truncatedbytes[1:]
    if truncatedbytes[0] == bytes([0x67]):
        G0 = Greeksymbols
        return(truncatedbytes[1:])
    elif truncatedbytes[0] == bytes([0x62]):
        G0 = Subscripts
        return(truncatedbytes[1:])
    elif truncatedbytes[0] == bytes([0x70]):
        G0 = Superscripts
        return(truncatedbytes[1:])
    elif truncatedbytes[0] == bytes([0x73]):
        G0 = Ascii
        return(truncatedbytes[1:])
    elif truncatedbytes[0] == bytes([0x28]) or truncatedbytes[0] == bytes([0x2c]):
        truncatedbytes = truncatedbytes[1:]
        G0 = charsetcodes[bytes.decode(truncatedbytes[0])]
        return(truncatedbytes[1:])
    elif truncatedbytes[0] == bytes([0x24]):
        G0 = Asiadict
        truncatedbytes = truncatedbytes[1:]
        if truncatedbytes[0] == bytes([0x2c]):
            truncatedbytes = truncatedbytes[2:]
            return(truncatedbytes)
        else:
            truncatedbytes = truncatedbytes[1:]
            return(truncatedbytes)
    elif truncatedbytes[0] == bytes([0x29]) or truncatedbytes[0] == bytes([0x2d]):
        truncatedbytes = truncatedbytes[1:]
        if truncatedbytes[0] == bytes([!]):
            G1 = Ansel
            return(truncatedbytes[2:])
        else:
            G1 = charsetcodes[bytes.decode(truncatedbytes[0])]
            return(truncatedbytes[1:])
    else:
        print('Error: Unknown escape sequence')

def utfcodelookup(byte):
#This will lookup the the utf8 code from the
#relevant dictionary and return those bytes
