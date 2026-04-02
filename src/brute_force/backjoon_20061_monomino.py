green = [[0]*4 for _ in range(6)]
blue = [[0]*4 for _ in range(6)]

score = 0

def drop(board, t, y):
    x = 0
    
    while True:
        if t == 1:
            if x == 5 or board[x+1][y]:
                break
        elif t == 2:
            if x == 5 or board[x+1][y] or board[x+1][y+1]:
                break
        else:
            if x == 4 or board[x+2][y]:
                break
        x += 1

    if t == 1:
        board[x][y] = 1
    elif t == 2:
        board[x][y] = board[x][y+1] = 1
    else:
        board[x][y] = board[x+1][y] = 1


def remove(board):
    global score
    new_board = [row[:] for row in board]
    idx = 5

    for i in range(5, -1, -1):
        if all(board[i]):
            score += 1
        else:
            new_board[idx] = board[i][:]
            idx -= 1

    for i in range(idx, -1, -1):
        new_board[i] = [0]*4

    return new_board


def light_area(board):
    cnt = 0
    for i in range(2):
        if any(board[i]):
            cnt += 1

    for _ in range(cnt):
        board.pop()
        board.insert(0, [0]*4)

    return board


N = int(input())

for _ in range(N):
    t, x, y = map(int, input().split())

    drop(green, t, y)
    green = remove(green)
    light_area(green)

    if t == 1:
        bt = 1
        by = x
    elif t == 2:
        bt = 3
        by = x
    else:
        bt = 2
        by = x

    drop(blue, bt, by)
    blue = remove(blue)
    light_area(blue)

cnt = 0
for i in range(6):
    cnt += sum(green[i])
    cnt += sum(blue[i])

print(score)
print(cnt)