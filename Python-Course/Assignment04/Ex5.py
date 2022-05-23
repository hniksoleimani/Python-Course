from math import floor
def fact(m):
    n = 1
    for i in range(1,floor(m/2)):
        n = i*n
        if n == m :
            print('Yes!') 
            break        
        elif n > m :
            print('No...!')
            break

num = int(input('Enter a number:'))
fact(num)
