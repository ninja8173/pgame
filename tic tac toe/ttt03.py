#보드 출력 함수
def prn_board(tb):
    for x in range(3):
        print("{}|{}|{}".format(tb[x][0], tb[x][1], tb[x][2]))
        print("-"*5)

#보드 초기화
turn = 'X'
board = [[' ', ' ',' '],
        [' ', ' ',' '],
        [' ', ' ',' ']]

#보드 출력
prn_board(board)

#9회 입력받기
for x in range(9):
    # 입력 좌표가 동일하면 재입력받기
    while True:
        y,x = map(int,input("좌표(y,x): ").split(','))
        if board[y][x] == ' ':
            break
        print("돌을 놓을 수 없습니다. 다시 지정하세요.")
    # 좌표에 돌 놓기
    board[y][x] = turn

    #돌 모양 바꾸기
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    prn_board(board)