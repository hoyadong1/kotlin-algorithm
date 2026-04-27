import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

board = []
fish = [None] * 17

for i in range(4):
    info = list(map(int, input().split()))
    temp = []
    for j in range(4):
        fish_num = info[j * 2]
        fish_d = info[j * 2 + 1] - 1
        temp.append([fish_num, fish_d])
        fish[fish_num] = (i, j)

    board.append(temp)


def fish_move(board, fish, sx, sy):
    for i in range(1, 17):
        if fish[i] == None:
            continue

        x, y = fish[i]
        d = board[x][y][1]

        for _ in range(8):
            nx, ny = x + dx[d], y + dy[d]

            if (0 <= nx < 4 and 0 <= ny < 4) and not (nx == sx and ny == sy):
                target = board[nx][ny][0]

                board[x][y][1] = d
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

                fish[i] = (nx, ny)
                if target != -1:
                    fish[target] = (x, y)
                break
            d = (d + 1) % 8


answer = 0


def dfs(board, fish, sx, sy, total):
    global answer

    board = copy.deepcopy(board)
    fish = copy.deepcopy(fish)

    num, d = board[sx][sy]
    total += num
    answer = max(answer, total)

    fish[num] = None
    board[sx][sy][0] = -1

    fish_move(board, fish, sx, sy)

    for step in range(1, 4):
        nx, ny = sx + dx[d] * step, sy + dy[d] * step

        if 0 <= nx < 4 and 0 <= ny < 4:
            if board[nx][ny][0] != -1:
                dfs(board, fish, nx, ny, total)


dfs(board, fish, 0, 0, 0)
print(answer)
