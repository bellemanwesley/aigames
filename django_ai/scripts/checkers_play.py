from random import randint
import sys
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts/"))
import database as db

def list_moves(board, team):
    regular_piece = team+2
    king_piece = team+3
    direction = team*-1

    non_taking_moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            available_squares = []
            if board[i][j] == king_piece:
                if i+1 in range(8) and j+1 in range(8):
                    available_squares.append([i+1,j+1])
                if i+1 in range(8) and j-1 in range(8):
                    available_squares.append([i+1,j-1])
                if i-1 in range(8) and j+1 in range(8):
                    available_squares.append([i-1,j+1])
                if i-1 in range(8) and j-1 in range(8):
                    available_squares.append([i-1,j-1])
            if board[i][j] == regular_piece:
                if i+direction in range(8) and j+1 in range(8):
                    available_squares.append([i+1,j+1])
                if i+direction in range(8) and j-1 in range(8):
                    available_squares.append([i+1,j-1])
            for x in available_squares:
                if board[x[0]][x[1]] == 0:
                    non_taking_moves.append([[i,j],[x[0],x[1]]])
    return non_taking_moves

def decide_move(moves, strengths):
    x = randint(0,len(moves)-1)
    return moves[x]
    
def make_move(board,move):
    if board[move[0][0]][move[0][1]]%2 == 1 and move[1][0] in [0,7]:
        board[move[1][0]][move[1][1]] = board[move[0][0]][move[0][1]] +1
    else:
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
    if len(moves) == 0:
        return "loss"
    move = decide_move(moves,0)
    board = make_move(board,move)
    for i in range(64):
        row = i//8
        col = i%8
        board_l[i] = str(board[row][col])
    board_str = ",".join(board_l)
    return board_str