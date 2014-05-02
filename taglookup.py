# (C) 2014 James Stephenson

with open('MARC21bibfieldlist.txt', 'rt') as infile:
    tagdata = infile.read()

#isnine take a MARC tag and returns True if that tag is for local use
def isnine(tag):
    for number in tag:
        if number == '9':
            return(True)
    return(False)

#gettag() takes a MARC tag and returns a string describing that tag
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

#getsubtags() takes a MARC tag as the first argument and a list of subtags
#as the 2nd argument.  It returns a list of strings describing the subtags
def getsubtags(maintag, subtagrequests):
    if isnine(maintag) is True:
        return(subtagrequests)
    current = 0
    maintag = maintag + ' - '
    subtagreply = []
    while tagdata[current:current + 6] != maintag:
        current = current + 1
    mainloc = current
    for item in subtagrequests:
        subtagrequest = '$' + item + ' - '
        subanswer = ""
        while tagdata[current:current + 5] != subtagrequest:
            current = current + 1
        while tagdata[current] != '\n':
            subanswer = subanswer + tagdata[current]
            current = current + 1
        current = mainloc
        subtagreply.append(subanswer)
    return(subtagreply)
