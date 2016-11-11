# Első Python script
# Fibonacci-sort írat ki, azaz egy olyan számsort, aminek minden tagja
# az előző két tag összege.
# a & b az egymást követő tagok számolására valók # c egy számláló
# az első tag kiíratása
# összesen 15 tagot íratunk ki

a, b, c = 1, 1, 1
print (1)
while c<15:
            a, b, c = b, a+b, c+1
            print (b)
