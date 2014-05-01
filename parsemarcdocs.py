strong = '<strong>Subfield Codes</strong>'
tag = ""
subtag = ""
current = 0
while marcdata[current:current + 4] != '<h1>':
    current = current + 1
while marcdata[current:current + 5] != '</h1>':
    tag = tag + marcdata[current]
    current = current + 1
print(tag)
while marcdata[current:current + 6] != '<table':
    current = current + 1
while marcdata[current:current + len(strong)] != strong:
    current = current + 1
while marcdata[current:current + 8] != '</table>':
    if marcdata[current] == '$':
        while marcdata[current] != '<':
            subtag = subtag + marcdata[current]
            current = current + 1
        print(subtag)
        subtag = ""
    else:
        current = current + 1
