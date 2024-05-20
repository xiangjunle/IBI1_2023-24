def chocolate(x,y):
    z=x//y
    return z
x=int(input('the total money that the user has:'))
y=int(input('the price of one chocolate bar:'))
z=str(chocolate(x,y))
print('you are able to afford '+z+' chocolate bars at the supermarket')
