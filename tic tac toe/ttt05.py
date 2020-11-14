# 보드 출력 함수
def prn_board(tb):
    for x in range(3):
        print("{}|{}|{}".format(tb[x][0], tb[x][1], tb[x][2]))

# 판정 함수
def judge(y, x):
    win = False
    if board[y][0] == turn and board[y][1] == turn and board[y][2] == turn:
        win = True
    elif board[0][x] == turn and board[1][x] == turn and board[2][x] == turn:
        win = True
    elif y-x == 0:
        if board[0][0] == turn and board[1][1] == turn and board[2][2] == turn:
            win = True
    if y-x == 0 or abs(y - x)==2:
        if board[0][2] == turn and board[1][1] == turn and board[2][0] == turn:
            win = True
    return win

# 변수 초기화
turn = 'X'
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
msg = "무승부"
# 게임 루프
for x in range(9):
    while True:
        # 좌표 입력 받기
        y, x = map(int,input("좌표(y x): ").split(','))
        if board[y][x] == ' ':
            break
        print("돌을 놓을 수 없습니다. 다시 지정해주세요.")
    # 돌 놓기
    board[y][x] = turn
    prn_board(board)

    # 판정
    if judge(y, x):
        msg = turn + "의 승리"
        break

    # 돌 모양 변경
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print(msg)




#