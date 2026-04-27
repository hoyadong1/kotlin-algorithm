h, w, n = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(h)]

top = 1
bottom = 6
east = 3
west = 4
north = 2
south = 5

dir = 0
cur_p = [0, 0]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def move():
    global cur_p, dir

    x, y = cur_p
    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 0 or nx >= h or ny < 0 or ny >= w:
        dir = (dir + 2) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]

    cur_p = [nx, ny]

    re_dice()

    return nx, ny


def re_dice():
    global top, bottom, east, west, north, south

    if dir == 0:
        top, bottom, east, west = west, east, top, bottom
    elif dir == 2:
        top, bottom, east, west = east, west, bottom, top
    elif dir == 1:
        top, bottom, north, south = north, south, bottom, top
    elif dir == 3:
        top, bottom, north, south = south, north, top, bottom


def change_dir(x, y):
    global bottom, dir

    if bottom > table[x][y]:
        dir = (dir + 1) % 4
    elif bottom < table[x][y]:
        dir = (dir - 1) % 4


def score_cal(x, y):
    score = 1
    num = table[x][y]

    visited = [[False] * w for _ in range(h)]
    visited[x][y] = True

    dirs = [(0,1), (1,0), (0,-1), (-1,0)]

    def dfs(x, y):
        nonlocal score

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if visited[nx][ny]:
                continue

            if table[nx][ny] == num:
                visited[nx][ny] = True
                score += 1
                dfs(nx, ny)

    dfs(x, y)
    return score * num


answer = 0

for _ in range(n):
    x, y = move()
    answer += score_cal(x, y)
    change_dir(x, y)

print(answer)