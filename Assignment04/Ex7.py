def lcm(x, y):
    for i in range(max(x,y), (x*y)+1):
        if (i % x == 0) & (i % y == 0):
            print(i)
            break

n = int(input('Enter X:'))
m = int(input('Enter Y:'))
lcm(m,n)