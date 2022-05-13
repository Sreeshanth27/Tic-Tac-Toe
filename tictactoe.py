def display_board(board):
    list1 = [board[7],board[8],board[9]]
    list2 = [board[4],board[5],board[6]]
    list3 = [board[1],board[2],board[3]]
    print(f'{board[7]}  |  {board[8]}  |  {board[9]}')
    print(f'---|-----|---')
    print(f'{board[4]}  |  {board[5]}  |  {board[6]}')
    print(f'---|-----|---')
    print(f'{board[1]}  |  {board[2]}  |  {board[3]}')

board = [0,' ',' ',' ',' ',' ',' ',' ',' ',' ']

def choice():
    choice = input('PLAYER1 CHOOSE YOUR SIDE: ')
    if choice == 'X' or choice == 'O':
        return choice
    else:
        while choice != 'X' and choice != 'O':
            choice = input('PLAYER1 CHOOSE YOUR SIDE: ')
            if choice == 'X' or choice == 'O':
                break
        return choice

def game_winner():
    if(board[1] == board[2] == board[3] == 'X' or board[1] == board[2] == board[3] == 'O'):
        return True
    elif(board[4] == board[5] == board[6] == 'X' or board[4] == board[5] == board[6] == 'O'):
        return True
    elif(board[7] == board[8] == board[9] == 'X' or board[7] == board[8] == board[9] == 'O'):
        return True
    elif(board[1] == board[4] == board[7] == 'X' or board[1] == board[4] == board[7] == 'O'):
        return True
    elif(board[2] == board[5] == board[8] == 'X' or board[2] == board[5] == board[8] == 'O'):
        return True
    elif(board[3] == board[6] == board[9] == 'X' or board[3] == board[6] == board[9] == 'O'):
        return True
    elif(board[1] == board[5] == board[9] == 'X' or board[1] == board[5] == board[9] == 'O'):
        return True
    elif(board[3] == board[5] == board[7] == 'X' or board[3] == board[5] == board[7] == 'O'):
        return True
    else:
        return False
    
def position_choose_p1():
    pos1 = int(input('PLAYER1 CHOOSE A POSITION: '))
    return pos1
def position_choose_p2():
    pos2 = int(input('PLAYER2 CHOOSE A POSITION: '))
    return pos2

remaining = [1,2,3,4,5,6,7,8,9]

p1 = choice()
if p1 == 'X':
    p2 = 'O'
else:
    p2 = 'X'
while len(remaining) != 0:
    x1 = position_choose_p1()
    remaining.remove(x1)
    board[x1] = p1
    display_board(board)
    if(game_winner() == True):
        print('PLAYER1 WINS')
        break
    
    x2 = position_choose_p2()
    remaining.remove(x2)
    board[x2] = p2
    display_board(board)
    if(game_winner() == True):
        print('PLAYER2 WINS')
        break