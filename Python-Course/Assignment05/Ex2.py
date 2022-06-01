import time
from colorama import init, Fore, Back, Style
init(autoreset = True)
def status():
        
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                print(Fore.GREEN + board[i][j],end=' ')
            elif board[i][j] == 'O':
                print(Fore.RED + board[i][j],end=' ')
            else:
                print(board[i][j],end=' ')
        print()

def check():
    if board[0][0] =='X' and board[0][1] == 'X' and board[0][2] =='X':
        print(Fore.WHITE + 'Player1 wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)        
        exit()
    elif board[1][0] =='X' and board[1][1] == 'X' and board[1][2] =='X':
        print('Player1 wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)        
        exit()
    elif board[2][0] =='X' and board[2][1] == 'X' and board[2][2] =='X':
        print('Player1 wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)        
        exit()
    elif board[0][0] =='X' and board[1][0] == 'X' and board[2][0] =='X':
        print('Player1 wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)        
        exit()
    elif board[0][1] =='X' and board[1][1] == 'X' and board[2][0] =='X':
        print('Player1 wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)        
        exit()
    elif board[0][2] =='X' and board[1][2] == 'X' and board[2][2] =='X':
        print('Player1 wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)        
        exit()
    elif board[0][0] =='X' and board[1][1] == 'X' and board[2][2] =='X':
        print('Player1 wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)        
        exit()
    elif board[0][2] =='O' and board[1][1] == 'O' and board[2][0] =='O':
        print(player, 'wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)
        exit()
    elif board[0][0] =='O' and board[1][1] == 'O' and board[2][2] =='O':
        print(player,'wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)
        exit()
    elif board[0][2] =='O' and board[1][1] == 'O' and board[2][0] =='O':
        print(player, 'wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)
        exit()
    elif board[0][0] =='O' and board[0][1] == 'O' and board[0][2] =='O':
        print(player, 'wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)        
        exit()
    elif board[1][0] =='O' and board[1][1] == 'O' and board[1][2] =='O':
        print(player,'wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)
        exit()
    elif board[2][0] =='O' and board[2][1] == 'X' and board[2][2] =='X':
        print(player, 'wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)
        exit()
    elif board[0][0] =='O' and board[1][0] == 'O' and board[2][0] =='O':
        print(player, 'wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)
        exit()
    elif board[0][1] =='O' and board[1][1] == 'O' and board[2][0] =='O':
        print(player, 'wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)
        exit()
    elif board[0][2] =='O' and board[1][2] == 'O' and board[2][2] =='O':
        print(player, 'wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)
        exit()
    elif board[0][0] =='O' and board[1][1] == 'O' and board[2][2] =='O':
        print(player, 'wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)
        exit()
    elif board[0][2] =='O' and board[1][1] == 'O' and board[2][0] =='O':
        print(player, 'wins ...!')
        end = time.time()
        elapsed = end - begin
        print('Elapsed time =', elapsed)
        exit()
board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]
def player1(turn):
    print('Player1')
    while True:
        row = int(input('Enter row:'))
        col = int(input('Enter Column:'))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == '_':
                board[row][col] = 'X'
                turn+=1
                if turn < 9 :
                    print('move number---------------------->',turn)
                    return turn
                    
                else:
                    print('Out of moves,Game Over...!') 
                    end = time.time()
                    elapsed = end - begin
                    print('Elapsed time =', elapsed)
                    break   
                    
                
            else:
                print('Cell is not empty.')
        else:
            print('Invalid input.')

def computer(turn):
    print('Computer')
    while True:
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    turn+=1
                    if turn < 9:
                        print('move number---------------------->',turn)
                        return turn
                    else:
                        print('Out of moves,Game Over...!') 
                        end = time.time()
                        elapsed = end - begin
                        print('Elapsed time =', elapsed)
                        break   

                



def player2(turn):
    print('Player2')
    while True:
        row = int(input('Enter row:'))
        col = int(input('Enter Column:'))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == '_':
                board[row][col] = 'O'
                turn+=1
                if turn < 9 :
                    print('move number---------------------->',turn)
                    return turn
                    
                else:
                    print('Out of moves,Game Over...!') 
                    end = time.time()
                    elapsed = end - begin
                    print('Elapsed time =', elapsed)
                    break   
                    
                
            else:
                print('Cell is not empty.')
        else:
            print('Invalid input.')

begin = time.time()
player = ''
ply = int(input('Enter number of players[1-2]:'))
status()
count = 0
while count < 10 :

    if ply == 1:
        count = player1(count)
        player = 'Player1'
        status()
        check()
        count = computer(count)
        player = 'Computer'
        status()
        check()
    elif ply == 2:
        count = player1(count)
        player = 'Player1'
        status()
        check()
        count = player2(count)
        player = 'Player2'
        status()
        check()
    else:
        print('Invalid input')

    

            

 
   