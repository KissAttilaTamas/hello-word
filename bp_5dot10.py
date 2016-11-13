st="ruff"
i=1
d=""
print(st,i)
while i<=len(st):
    d=d+st[(len(st)-i)]
    i=i+1
if st==d :
    print(st, " is palindrom")
else:
    print(st, " is not palindrom")
        
