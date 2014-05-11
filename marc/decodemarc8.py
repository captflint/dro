# (C) 2014 - James Stephenson

from MARC8dicts import Ascii, Ansel, Greeksymbols, Subscripts, Superscripts, Basichebrew, Basiccyrillic, Extendedcyrillic, Basicarabic, Extendedarabic, Basicgreek, Asiadict

# Define some character set properties
charsetcodes = {'3': Basicarabic, '4': Extendedarabic, 'B': Ascii, '!E': Ansel, '1': Asiadict, 'N': Basiccyrillic, 'Q': Extendedcyrillic, 'S': Basicgreek, '2': Basichebrew}

combiningchars = "ְֱֲֳִֵֶַָֹֻּֿׁﬞًٌٍَُِّْ̧̨̣̤̥̳̲̦̜̮̉̀́̂̃̄̆̇̈̌̊̋̐̓̆̌̀́̈͂̓̔̕͡͠ͅ"

G0 = Ascii
G1 = Ansel
utfstring = bytes('', 'utf-8')



def convertmarc8(marcbytes):
    global utfstring
    utfstring = bytes('', 'utf-8')
    while len(marcbytes) > 0:
        if marcbytes[0] == int('0x1b', base = 16):
            marcbytes = changecharset(marcbytes)
            print('changing charset')
        else:
            if G0 == Ascii and marcbytes[0] <= 127:
                utfstring += bytes([marcbytes[0]])
                marcbytes = marcbytes[1:]
            elif G0 == Asiadict:
                marcbytes = asiadecode(marcbytes)
            else:
                utfstring += utfcodelookup(marcbytes[0])
                marcbytes = marcbytes[1:]
                print(bytes.decode(utfstring))
    return(cleanup(utfstring))

def cleanup(string):
#This function will put combining characters in the
#correct positions and return a utf-8 string
    string = bytes.decode(string, 'utf-8')
    combining = ''
    returnstring = ''
    while len(string) != 0:
        if string[0] not in combiningchars:
            returnstring += string[0]
            string = string[1:]
            if len(combining) > 0:
                returnstring += combining
                combining = ''
        else:
            combining += string[0]
            string = string[1:]
    return(returnstring)

def changecharset(truncatedbytes):
#This will change the character set and return
#the bites minus the escape sequence
    global G0
    global G1
    truncatedbytes = truncatedbytes[1:]
    if truncatedbytes[0] == int('0x67', base = 16):
        G0 = Greeksymbols
        return(truncatedbytes[1:])
    elif truncatedbytes[0] == int('0x62', base = 16):
        G0 = Subscripts
        return(truncatedbytes[1:])
    elif truncatedbytes[0] == int('0x70', base = 16):
        G0 = Superscripts
        return(truncatedbytes[1:])
    elif truncatedbytes[0] == int('0x73', base = 16):
        G0 = Ascii
        return(truncatedbytes[1:])
    elif truncatedbytes[0] == int('0x28', base = 16) or truncatedbytes[0] == int('0x2c', base = 16):
        truncatedbytes = truncatedbytes[1:]
        G0 = charsetcodes[chr(truncatedbytes[0])]
        return(truncatedbytes[1:])
    elif truncatedbytes[0] == int('0x24', base = 16):
        G0 = Asiadict
        truncatedbytes = truncatedbytes[1:]
        if truncatedbytes[0] == int('0x2c', base = 16):
            truncatedbytes = truncatedbytes[2:]
            return(truncatedbytes)
        else:
            truncatedbytes = truncatedbytes[1:]
            return(truncatedbytes)
    elif truncatedbytes[0] == int('0x29', base = 16) or truncatedbytes[0] == int('0x2d', base = 16):
        truncatedbytes = truncatedbytes[1:]
        if truncatedbytes[0] == ord('!'):
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
    returnval = bytes('', 'utf-8')
    if byte <= 127:
        charset = G0
    else:
        charset = G1
    utfchar = charset[hex(byte)[2:].upper()]
    if utfchar == None:
        return(returnval)
    while len(utfchar) > 0:
        twochars = int('0x' + utfchar[0:2], base = 16)
        returnval += bytes([twochars])
        utfchar = utfchar[2:]
    return(returnval)

def asiadecode(asiabytes):
#This function will decode multibyte asian characters
    global utfstring
    utfbytes = bytes('', 'utf-8')
    while ord(asiabytes[0]) != 0x1b:
        utfchar = hex(asiabytes[0])[2:] + hex(asiabytes[1])[2:] + hex(asiabytes[2])[2:]
        utfchar = asiadict[utfchar.upper()]
        if utfchar == None:
            utfbytes = bytes('', 'utf-8')
            asiabytes = asiabytes[3:]
        else:
            while len(utfchar) > 0:
                twochars = int('Ox' + utfchar[0:2], base = 16)
                utfbytes += bytes([twochars])
                utfchar = utfchar[2:]
            utfstring += utfbytes
            utfbytes = bytes('', 'utf-8')
            asiabytes = asiabytes[3:]
    return(asiabytes)
