import xml.etree.ElementTree as ET
tree = ET.parse('MARC8codetables.xml')
root = tree.getroot()
setlist = []

combininglist = []
for code in root.iter('code'):
    if code.find('isCombining') != None:
        combininglist.append(code.find('utf-8').text)
print(combininglist)
