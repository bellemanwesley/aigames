from random import randint
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, "scripts/"))
import database as db

def board_to_string(board):
    board_int = int(board,5)
    board_str = ""
    while board_int > 0:
        board_str += chr(board_int % 256)
        board_int = board_int // 256
    return board_str

def string_to_board(string):
    board_int = 0
    string_rev = string[::-1]
    for i in range(len(string)):
        board_int = board_int * 256
        board_int += ord(string_rev[i])
    board = ""
    while board_int > 0:
        board += str(board_int%5)
        board_int = board_int // 5
    board = board[::-1]
    if len(board) < 32:
        board = "0" * (32-len(board)) + board
    return board

def board_to_hex(board):
    board_int = int(board,5)
    return hex(board_int)[2:]

def hex_to_board(string):
    board_int = int(string,16)
    board = ""
    while board_int > 0:
        board = str(board_int%5) + board
        board_int = board_int // 5
    return board



def main():
    return 0