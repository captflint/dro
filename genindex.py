with open('MARC21bibfieldlist.txt', 'rt') as infile:
    marcdata = infile.read()

def stringify(tag):
    if tag < 10:
        return('00' + str(tag))
    elif tag < 100:
        return('0' + str(tag))
    else:
        return(str(tag))

testlist = [0, 1, 9, 10, 99, 100, 999]
for item in testlist:
    print(item, '\t', stringify(item))
