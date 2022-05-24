from math import sqrt
# def delta(a,b,c):
def EQN(a,b,c):
    delta = (b**2)-(4*a*c)
    if delta <0: 
        print('No Answer')
    elif delta == 0:
        x = -b/a
        print('1 Answer:', x)

    elif delta > 0:
        x1 = (-b+sqrt(delta))/2*a 
        x2 = (-b-sqrt(delta))/2*a
        print('2 Answers', x1, x2)



m = int(input('Enter a:'))
n = int(input('Enter b:'))
o = int(input('Enter c:'))
EQN(m,n,o)
