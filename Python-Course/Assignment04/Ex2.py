from math import sqrt

def EQN(a,b,c):
    delta = (b*2)-(4*a*c)
    ans1 = (-b+sqrt(delta))/2*a 
    ans2 = (-b-sqrt(delta))/2*a
    print(ans1)
    print(ans2)


m = int(input('Enter a:'))
n = int(input('Enter b:'))
o = int(input('Enter c:'))
EQN(m,n,o)
