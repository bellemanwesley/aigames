# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import json
import sys
sys.path.insert(0, '/home/ubuntu/aigames/scripts/')
import tictactoe_play

def home(request):
	return(render(request,'home.html',{}))
	
def tictactoe(request):
    if request.method == "POST":
        board_str = request.POST["board"]
        board_l = board_str.split(",")
        board = [[0,0,0],[0,0,0],[0,0,0]]
        print(board_str)
        for i in range(9):
            row = i//3
            col = i%3
            board[row][col] = int(board_l[i])
        print(board)
        my_list = tictactoe_play.return_move(board, -1)
        return HttpResponse(str(my_list),content_type="text/plain")
    else:
        return(render(request,'tictactoe.html',{}))
    
def checkers(request):
    return(render(request,'checkers.html',{}))