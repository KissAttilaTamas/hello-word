st="dfddfdfdffgvfsedfsdf"
i=0
print(st,i)
while i<len(st):
    print(i,st[i])
    if st[i]=="e":
        print('found at position',i+1)
    i=i+1
print(i)
