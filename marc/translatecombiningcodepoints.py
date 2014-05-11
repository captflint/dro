from MARC8dicts import combininglist

combiningstring = ''

for codepoint in combininglist:
    if codepoint != None:
        codebytes = bytes('', 'utf-8')
        while len(codepoint) > 0:
            twochar = '0x' + codepoint[:2]
            codebytes += bytes([int(twochar, base = 16)])
            codepoint = codepoint[2:]
        combiningstring += bytes.decode(codebytes)

print(combiningstring)

