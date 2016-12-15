def acsiitable(e,v):
    while e<=v:
        if 'a'<=chr(e)<='z':
            k=chr(e-32)
        elif 'A'<=chr(e)<='Z':
            k=chr(e+32)
        else:
            k=''
        print(e,': "',chr(e),'"', k)
        e=e+1
       
acsiitable(32,126)
