testrecord = """01795cam a22003854a 45000010009000000050017000090080041000269060045000679250044001129550179001560100017003350200018003520200015003700400018003850420009004030500025004120820014004371000020004512450037004712500012005082600048005203000021005685000011005895000035006005200291006356500024009266500031009506500027009816500029010086100057010376510037010948560106011318560091012378560081013281522138720100806172336.0080317s2008    nyu    d      000 1 eng    a7bcbccorignewd1eecipf20gy-gencatlg0 aacquireb2 shelf copiesxpolicy default  alb18 2008-03-17ilb18 2008-03-17elb18 2008-03-17 to CIPaps15 2008-06-19 2 copies rec'd., to CIP ver.flf27 2008-08-11glf27 2008-08-11 to BCCDdxc09 2010-08-06 restored 042  a  2008001827  a9780765319852  a0765319853  aDLCcDLCdDLC  alcac00aPZ7.D66237bLit 200800a[Fic]2221 aDoctorow, Cory.10aLittle brother /cCory Doctorow.  a1st ed.  aNew York :bTom Doherty Associates,cc2008.  a382 p. ;c22 cm.  a"Tor."  a"A Tor Teen book"--T.p. verso.  aAfter being interrogated for days by the Department of Homeland Security in the aftermath of a major terrorist attack on San Francisco, California, seventeen-year-old Marcus, released into what is now a police state, decides to use his expertise in computer hacking to set things right. 1aTerrorismvFiction. 1aComputer hackersvFiction. 1aCivil rightsvFiction. 1aCounterculturevFiction.11aUnited States.bDept. of Homeland SecurityvFiction. 1aSan Francisco (Calif.)vFiction.423Contributor biographical informationuhttp://www.loc.gov/catdir/enhancements/fy0828/2008001827-b.html423Publisher descriptionuhttp://www.loc.gov/catdir/enhancements/fy0828/2008001827-d.html413Sample textuhttp://www.loc.gov/catdir/enhancements/fy0901/2008001827-s.html"""

# This funtion parses the directory of the given MARC record.  Each record
# has a directory that starts on character 24 (starting numbering at zero).
# Each directory entry is 12 character in length.  The first three
# characters are the field tag, the next four are the length of the field,
# the last five are the starting position of the field.
# takes a MARC record, returns a list of lists containing the directory
def readdir(record):
# we create an empty list; this will eventually be a list of lists.
    directory = []
    current = 24 #the fist character of the directory
# the directory (and each field) is terminated with ascii 0x1e
    while record[current] != "":
        tag = record[current:current + 3]
        length = record[current + 3:current + 7]
        start = record[current + 7:current + 12]
# de is a list containing a single directory entry, we append this list to
# the directory list of lists
        de = [tag, int(length), int(start)]
        directory.append(de)
        current = current + 12
    return(directory)

# takes a MARC record and a list from readdir() and displays the record
def displayrecord(record, dirlist):
# the next 4 lines skip to the actual field entries
    current = 24
    while record[current] != "":
        current = current + 1
    current = current + 1
    for de in dirlist:
        print(de[0])
        print(record[current + de[2]:current + de[2] + de[1]])
        print("\n")

displayrecord(testrecord, readdir(testrecord))
