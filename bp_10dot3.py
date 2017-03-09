def indexes(sztring,kar):
    x=0
    talal=0
    print (sztring,kar)
    while x<len(sztring):
        if sztring[x]==kar:
            return x
        elif x==len(sztring)-1:
            return -1
        x=x+1

print(indexes('elso proba',"x"))     

