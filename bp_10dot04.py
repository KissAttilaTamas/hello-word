def megtalal(sztring, kar, kezd):
    i=kezd-1
    x=0
    while i<=len(sztring)-1:
        if sztring[i]==kar:
            return x
        elif i==len(sztring)-1:
            return 99
        else:
            pass
        print(i,":",sztring[i])
        i=i+1
        x=x+1



print(megtalal("César & Cléopâtre", "t", 8))
