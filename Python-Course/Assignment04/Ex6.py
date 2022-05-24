def gcd(x, y):
    for i in range(1,min(x+1,y+1)):
        if(x%i==0) & (y%i==0):
            print(i)
            

a = int(input('Enter A:'))
b = int(input('Enter B:'))

gcd(a,b)

