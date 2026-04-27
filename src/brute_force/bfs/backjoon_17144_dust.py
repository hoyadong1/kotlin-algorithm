from collections import deque

R, C, T = map(int, input().split())

Map = [list(map(int, input().split())) for _ in range(R)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

purifier = 0

for i in range(R):
    if Map[i][0] == -1:
        purifier = i
        break


def spread_dust():
    global Map
    q = deque()

    for i in range(R):
        for j in range(C):
            if (Map[i][j] // 5) > 0:
                q.append((i, j, Map[i][j]))

    while q:
        x, y, val = q.popleft()
        avg = val // 5

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < R and 0 <= ny < C:
                if Map[nx][ny] != -1:
                    Map[nx][ny] += avg
                    val -= avg
                    Map[x][y] -= avg


def count_dust():
    dust = 0
    for i in range(R):
        for j in range(C):
            if Map[i][j] != -1:
                dust += Map[i][j]

    return dust


def purify():
    global Map

    up = purifier
    down = purifier + 1

    for i in range(up - 1, 0, -1):
        Map[i][0] = Map[i - 1][0]

    for j in range(C - 1):
        Map[0][j] = Map[0][j + 1]

    for i in range(up):
        Map[i][C - 1] = Map[i + 1][C - 1]

    for j in range(C - 1, 1, -1):
        Map[up][j] = Map[up][j - 1]

    Map[up][1] = 0

    for i in range(down + 1, R - 1):
        Map[i][0] = Map[i + 1][0]

    for j in range(C - 1):
        Map[R - 1][j] = Map[R - 1][j + 1]

    for i in range(R - 1, down, -1):
        Map[i][C - 1] = Map[i - 1][C - 1]

    for j in range(C - 1, 1, -1):
        Map[down][j] = Map[down][j - 1]

    Map[down][1] = 0


for _ in range(T):
    spread_dust()
    purify()

print(count_dust())
