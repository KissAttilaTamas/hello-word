t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június','Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
x=0
t3=[]
print(t1[x])
while x<len(t1):
    t3.append(t2[x])
    t3.append(str(t1[x]))
    print(t3)
    x=x+1
print(t3)    
