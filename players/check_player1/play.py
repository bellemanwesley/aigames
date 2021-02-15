def board_to_string(board):
    board_int = int(board,5)
    board_str = ""
    while board_int > 0:
        board_str += chr(board_int % 256)
        board_int = board_int // 256
    return board_str

print(board_to_string("4"*32))