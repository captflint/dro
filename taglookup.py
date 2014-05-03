# (C) 2014 James Stephenson

with open('MARC21bibfieldlist.txt', 'rt') as infile:
    tagdata = infile.read()

from tagindex import tagindex

#gettag() takes a MARC tag and returns a string describing that tag
def gettag(tagrequest):
    if tagrequest not in tagindex:
        return(tagrequest)
    else:
        current = tagindex[tagrequest]
        tagreply = ""
        while tagdata[current] != '\n':
            tagreply = tagreply + tagdata[current]
            current = current + 1
        return(tagreply)

#getsubtags() takes a MARC tag as the first argument and a list of subtags
#as the 2nd argument.  It returns a list of strings describing the subtags
def getsubtag(maintag, subtagrequest):
    if maintag not in tagindex:
        return('$' + subtagrequest)
    else:
        current = tagindex[maintag]
        subtagreply = ""
        while tagdata[current:current + 5] != '$' + subtagrequest + ' - ':
            current = current + 1
        while tagdata[current] != '\n':
            subtagreply = subtagreply + tagdata[current]
            current = current + 1
        return(subtagreply)
