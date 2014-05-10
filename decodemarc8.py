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

def utfcodelookup(byte):
#This will lookup the the utf8 code from the
#relevant dictionary and return those bytes
