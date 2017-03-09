import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000', periods=8)

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

df = pd.DataFrame(np.random.randn(8, 3), index=index,columns=['A', 'B', 'C'])

wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],
           major_axis=pd.date_range('1/1/2000', periods=5),
     minor_axis=['A', 'B', 'C', 'D'])

wp[1,1::-2]
wp[1,1::-1]
wp[1,2::-1]
wp[1,1:2,2::-1]
wp[1,4::-2,4::-2] 
    
    
long_series = pd.Series(np.random.randn(1000))

long_series.head()
long_series.tail(3)

ures2=[]
xc=range(2,12000)
for r in xc:
    s=2
    while s<r:
        if r%s==0:
            ures2=ures2+r
    s=s+1
print(ures2)                    

