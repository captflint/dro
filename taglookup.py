with open('MARC21bibfieldlist.txt', 'rt') as infile:
    tagdata = infile.read()

def isnine(tag):
    for number in tag:
        if number == '9':
            return(True)
    return(False)

def gettag(tagrequest):
    if isnine(tagrequest) is True:
        return(tagrequest)
    current = 0
    tagrequest = tagrequest + ' - '
    tagreply = ""
    while tagdata[current:current + 6] != tagrequest:
        current = current + 1
    while tagdata[current] != '\n':
        tagreply = tagreply + tagdata[current]
        current = current + 1
    return(tagreply)

def getsubtag(maintag, subtagrequest):
    if isnine(maintag) is True:
        return(subtagrequest)
    current = 0
    maintag = maintag + ' - '
    subtagrequest = '$' + subtagrequest
    subtagreply = ""
    while tagdata[current:current + 6] != maintag:
        current = current + 1
    while tagdata[current:current + 2] != subtagrequest:
        current = current + 1
    while tagdata[current] != '\n':
        subtagreply = subtagreply + tagdata[current]
        current = current + 1
    return(subtagreply)
