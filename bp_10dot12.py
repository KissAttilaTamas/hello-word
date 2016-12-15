def kisbetu(ch):
    if 'a' <= ch <= 'z' :
        return 1
    else:
        return 0

def betu(ch):
    if 'a' <= ch <= 'z' :
        return 1
    elif 'A' <= ch <= 'Z' :
        return 2
    else:
        return 0

def szam(n):
    if type(n)==int:
        return 1
    elif type(n)==float:
        return 2
    else:
        return        0

print(kisbetu('z'))
print(betu('X'))
print(szam(8.1))
