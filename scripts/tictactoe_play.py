from random import random
from random import randint
import copy
import json
import sys

#STEP 2: Determine which moves you can make given state s
def find_moves(s):
    moves = []
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 0:
                moves.append([i,j])
    return moves
    
#STEP 3: Use Laplace's Law to determine which move to make
def decide_move(moves,strengths):
    selector_list = []
    for x in moves:
        move = str(move_transform(x))
        if move in strengths:
            strength = strengths[move]
        else:
            strength = [0,0]
        print(move,strength)
        selector_list.append(float(strength[0]+1)/float(strength[1]+2))
    selector_var = random()*sum(selector_list)
    selected = False
    print(selector_list)
    print(selector_var)
    for i in range(len(selector_list)):
        if selector_var < selector_list[i] and not selected:
            move = moves[i]
            selected = True
        selector_var -= selector_list[i]
    return move

#STEP 4: Make the move
def make_move(s, move, team):
    #Transform s and team based on the chosen move
    s[move[0]][move[1]] = team
    team = team * -1
    return s, team

#STEP 5: Determine the status of the game. If the game is over, determine the winner.
def game_status(s):
    #Return True if the game is not over
    #Return False if the game is over
    CONDITION = True
    for x in s:
        if x[0] == x[1] == x[2] != 0:
            CONDITION = False
            winner = x[0]
    for i in range(len(s[0])):
        if s[0][i] == s[1][i] == s[2][i] !=0:
            CONDITION = False
            winner = s[0][i]
    if s[0][0] == s[1][1] == s[2][2] != 0:
        CONDITION = False
        winner = s[0][0]
    if s[0][2] == s[1][1] == s[2][0] != 0:
        CONDITION = False
        winner = s[0][2]
    if CONDITION:
        return [True]
    else:
        return [False, winner]

#Helper A: Create a transformation from a move in moves to a string
def move_transform(move):
    move_t = ""
    for x in move:
        move_t += str(x)
    return int(move_t, 3)

#Helper B: Create a transformation from a state to a string
def state_transform(s):
    state = ""
    for x in s:
        for y in x:
            state += str(y+1)
    return int(state, 3)
    
def return_move(board, team):
    s = state_transform(board)
    moves = find_moves(board)
    with open("/home/ubuntu/aigames/scripts/files/tictactoe.json","r") as f:
        all_strengths = json.load(f)
    if s in all_strengths:
        strengths = all_strengths[s]
    else:
        strengths = {}
    move = decide_move(moves,strengths)
    return move
    
    
print(return_move([[1,0,0],[0,0,0],[0,0,0]],1))
