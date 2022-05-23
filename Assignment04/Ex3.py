a = int(input('Enter m:'))
b = int(input('Enter n:'))

def Multiplication(m,n):
    for i in range(1, m+1):
        for j in range(1, n+1):
            print((i*j), end = ' \t')
        print()


Multiplication(a, b)