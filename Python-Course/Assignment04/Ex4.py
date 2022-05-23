def Count(st):
    count=0
    for i in st:
        if i == ' ':
            count+=1
    print(count)



m = (input('Enter a statement:'))

Count(m)