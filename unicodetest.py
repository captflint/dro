print("This is a test of Python3's support of unicode")
teststr = "‽ Mi amas ŝin"
for char in teststr:
    print(char, bytes(char, 'utf-8'), len(bytes(char, 'utf-8')))
