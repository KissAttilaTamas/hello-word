def masol(longstring):
    x=1
    masol=''
    forditott=''
    print(x,longstring)
    while x<=int(len(longstring)/5)+1:
        if len(longstring)-(5*x)>=0:
            vag=longstring[len(longstring)-(5*x):len(longstring)-(x-1)*5]
        else:
            vag=longstring[0:y-5]
        print(vag)
        forditott=forditott+vag
        y=len(longstring)-(x-1)*5
        print(x,y,vag)
        x=x+1
    return forditott

t='11111222223333344444555556666'
print (t)
print(masol(t))
