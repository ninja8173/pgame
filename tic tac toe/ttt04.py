# 보드 출력 함수
def prn_board(tb):
    for x in range(3):
        print("{}|{}|{}".format(tb[x][0], tb[x][1], tb[x][2]))

# 변수 초기화
turn = 'X'
board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

# 게임 루프
for x in range(9):
    while True:
        #좌표 입력 받기
        y,x = map(int,input("좌표(y x): ").split(','))
        #빈 칸이면 돌 놓기 후 보드 출력
        if board[y][x] == ' ':
            break
        print("돌을 놓을 수 없습니다. 다시 지정해주세요.")
    board[y][x] = turn
    prn_board(board)

    # 승리 판정
    if board[y][0] == turn and board[y][1] == turn and board[y][2] == turn:
        break
    elif board[0][x] == turn and board[1][x] == turn and board[2][x] == turn:
        break

    # 턴(돌) 변경하기
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'