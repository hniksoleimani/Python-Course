def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    print(x)

a = int(input('Enter A:'))
b = int(input('Enter B:'))

gcd(a,b)
