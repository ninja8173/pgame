# 보드 출력 함수 def prn_board(board)

def prn_board(board):
    for x in range(3):
        print("{}|{}|{}".format(board[x][0], board[x][1], board[x][2]))
        print("-"*5)

# 보드 초기화

board = [[' ', ' ',' '],
        [' ', ' ',' '],
        [' ', ' ',' ']]

# 보드 출력

prn_board(board)