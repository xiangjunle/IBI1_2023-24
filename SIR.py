import numpy as np 
import matplotlib . pyplot as plt 
N=10000
beta=0.3
gamma=0.05
s=[9999]
i=[1]
r=[0]
time=[0]
for o in range(1000):
    time.append(o+1)
    x=i[o]*s[o]*beta/N+i[o]-i[o]*gamma
    if s[o]<=0:
        i.append(i[o]-i[o]*gamma)
    else:    
        i.append(x)
    y=i[o]*gamma+r[o]
    if y >=10000:
        r.append(10000)
    else:
        r.append(y)
    z=s[o]-x
    if z <= 0:
        s.append(0)
    else:
        s.append(z)
fig,ax = plt.subplots(figsize=(10,6))
ax.plot(s,c='b',lw=2,label='s')   
ax.plot(i,c='r',lw=2,label='i')
ax.plot(r,c='g',lw=2,label='r')
ax.set_xlabel('Day',fontsize=20)
ax.set_ylabel('xxx',fontsize=20)
ax.grid(1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend()
plt.show()
plt.clf()
