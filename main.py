import random
import sys

board=[i for i in range(0,9)]
winners=[(0,1,2),(3,4,5),(6,7,8),(0,4,8),(1,4,7),(2,4,6),(0,3,6),(2,5,8)]
moves=((1,3,7,9),(5,),(2,4,6,8))
player,computer='',''
tab=range(1,10)

def select_char():
    char=('X','O')
    return char[::1]

def print_board():
    x=1
    for i in board:
        end = ' | '
        if x%3==0:
            end=' \n'
            if i!=1:
                end+='---------\n'
        char = ' '
        if i in ('X','O'):
            char=i
        x+=1
        print(char,end=end)

def can_move(board,player,move):
    if board[move-1]==move-1 and move in tab:
        return True
    return False

def can_win(board,player,move):
    places=[]
    x=0
    for i in board:
        if (i==player):
            places.append(i)
        x+=1
    win=True
    for tup in winners:
        win = True
        for mv in tup:
            if board[mv] != player:
                win=False
                break
        if win == True:
            break
    return win

def make_move(board,player,move,undo=False):
    if can_move(board,player,move):
        board[move-1]=player
        win=can_win(board,player,move)
        if undo:
            board[move-1]=move-1
        return (True,win)
    return (False,False)

def space_exist():
    if board.count('X')+board.count('O')!=9:
        return True
    else:return False

def computer_turn():

    move=-1
    for i in range(1,10):
        if make_move(board,computer,i,True)[1]:
            move=i
            break

    if move ==-1:

        for i in range(1,10):
            if make_move(board,player,i,True)[1]:
                move = i
                break
    if move==-1:

        for tup in moves:
            for m in tup:
                if can_move(board,computer,m) and move==-1:
                    move=m
                    break
    return make_move(board,computer,move)

player,computer=select_char()
print('Player is [%s] and computer is [%s]'%(player,computer))
result="no winner"
while space_exist():
    print_board()
    print('Enter your move')
    move=int(input())
    moved,win=make_move(board,player,move)
    if not moved:
        print("invalid input")
        continue
    if win:
        result='Congrats'
        break
    elif computer_turn()[1]:
        result='You loss'
        break

print_board()
print(result)


