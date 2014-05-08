import xml.etree.ElementTree as ET
tree = ET.parse('MARC8codetables.xml')
root = tree.getroot()
setlist = []
for charset in root.iter('characterSet'):
    setlist.append(charset)

grouplist = []

for group in setlist[-1]:
    grouplist.append(group)

dictlist = []
for charset in setlist[:-1]:
    setdict = {}
    setdict['name'] = charset.attrib['name']
    setdict['ISOcode'] = charset.attrib['ISOcode']
    for code in charset:
        if code.tag == 'code':
            marc = code.find('marc').text
            utf = code.find('utf-8').text
            setdict[marc] = utf
    dictlist.append(setdict)
for dictionary in dictlist:
    print('\n\n', dictionary['name'])
    print(dictionary)

asiadict = {}
for group in grouplist:
    for code in group:
        if code.tag == 'code':
            marc = code.find('marc').text
            utf = code.find('utf-8').text
            asiadict[marc] = utf
print('\n\nasiadict')
print(asiadict)
