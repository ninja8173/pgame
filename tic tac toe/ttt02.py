#ttt_02

# 보드 출력 함수
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

# 입력 받기
for cnt in range(9):
    while True:
        x, y = map(int,input("좌표(x,y): ").split(','))
        #y, x 에 돌을 놓을 수 있는지 확인 후 가능하면 break로 빠져나오기
        if board[y][x] == ' ':
            board[y][x] = 'O'
            break
        print("돌을 놓을 수 없습니다. 다시 지정하세요.")

prn_board(board)