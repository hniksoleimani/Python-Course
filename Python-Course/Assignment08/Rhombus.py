# list = []
# for i in range(10):
#     list.append(' *'*i)
# print('\n'.join(list))    



def pyr(n):
    k = 2*n - 2
    blank = (n+1)*' '
    for i in range(0, n):
        print(blank, end = '')
        for j in range(0, k):
            print(end=" ")
        
        k = k - 1
        
        for j in range(0, i+1):
            
            print("* ", end="")
        
        print("\r")
    print((' '*((2*rows)-1))+'* '*(rows+1))    


    k = 2*n 

    for i in reversed(range(n)):
        
        for j in reversed(range(k)):
            print(end=" ")
        
        k = k + 1
        
        for j in range(0,i+1):
            
            print("* ", end="")
        
        print("\r")

        

rows = int(input('Enter number of rows:'))
pyr(rows)


