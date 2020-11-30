# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import json
import sys
sys.path.insert(0, '/home/ubuntu/aigames/scripts/')
import tictactoe_play
import checkers_play

def home(request):
	return(render(request,'home.html',{}))
	
def tictactoe(request):
    if request.method == "POST":
        board = request.POST["board"]
        my_list = tictactoe_play.return_move(board, -1)
        return HttpResponse(str(my_list),content_type="text/plain")
    else:
        return(render(request,'tictactoe.html',{}))
    
def checkers(request):
    if request.method == "POST":
        board = request.POST["board"]
        new_board = checkers_play.return_move(board, -1)
        return HttpResponse(new_board,content_type="text/plain")
    else:
        return(render(request,'checkers.html',{}))