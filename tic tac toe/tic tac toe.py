#tic tac toe text

#

#틱택토 게임

board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]
b = [[1,2,3],[4,5,6],[7,8,9]]
x=0
z=0
for x in range(3):
    print("%d%d|%d|" %(b[x][0] , b[x][1], b[x][2]))
    print("-")