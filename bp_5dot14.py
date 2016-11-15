t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június','Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
x=0
t11, t12=[],[]
print(t2[x])
while x<len(t2):
    if x % 2== 0:
        t11.append(t2[x])
    else:
        t12.append(t2[x])
    x=x+1
print(t2,"\n",t11,"\n",t12) 
