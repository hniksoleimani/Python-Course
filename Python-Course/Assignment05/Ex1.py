def Pascal(num): 
    triangle = [[1]]
    for i in range(num - 1):
        temp = [0] + triangle[-1] + [0]
        row = []
        for j in range(len(triangle[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        triangle.append(row)
    return triangle

n = int(input('Enter number of rows:'))
L = Pascal(n)
for i in range(n):
    print(L[i])