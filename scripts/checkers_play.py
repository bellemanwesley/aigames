from random import randint
import sys
sys.path.insert(0, '/home/ubuntu/aigames/scripts/')
import database as db

def list_moves(board, team):
    regular_piece = team*2-1
    king_piece = team*2
    take_moves = []
    return [[[2,0],[3,1]]]

def decide_move(moves, strengths):
    x = randint(0,len(moves)-1)
    return moves[x]
    
def make_move(board,move):
    board[move[1][0]][move[1][1]] = board[move[0][0]][move[0][1]]
    board[move[0][0]][move[0][1]] = 0
    return board

def return_move(board_str, team):
    board_l = board_str.split(",")
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            row.append(0)
        board.append(row)
    for i in range(64):
        row = i//8
        col = i%8
        board[row][col] = int(board_l[i])
    moves = list_moves(board,team)
    move = decide_move(moves,0)
    board = make_move(board,move)
    for i in range(64):
        row = i//8
        col = i%8
        board_l[i] = str(board[row][col])
    board_str = ",".join(board_l)
    return board_str