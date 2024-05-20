def year(x):
    x+=18
    if x <= 1986:
        z='a'
    else:
        if x <= 1994:
            z='b'
        else:
            if x <= 2005:
                z='c'
            else:
                z='d'
    return z                        
x=int(input("put the year in which that you was born:"))
y={'a':'Roger Moore','b':'Timothy Dalton','c':'Pierce Brosnan','d':'Daniel Craig'}
z=year(x)
print('your individual’s Bond actor is '+y[z])
    

