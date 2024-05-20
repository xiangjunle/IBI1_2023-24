x=input('Please input the DNA sequence here :')
n=0
for i in range(len(x)-6):
    seq=x[i:i+6]
    if seq =="GTGTGT" or seq=="GTCTGT":
        n+=1
print(n)




