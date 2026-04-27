N, M = map(int, input().split())
x, y, d = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

while True:
    if table[x][y] == 0:
        table[x][y] = 2
        count += 1

    cleaned = False

    for _ in range(4):
        d = (d - 1) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == 0:
            x, y = nx, ny
            cleaned = True
            break

    if cleaned:
        continue

    back = (d + 2) % 4
    nx = x + dx[back]
    ny = y + dy[back]

    if table[nx][ny] == 1:
        break
    else:
        x, y = nx, ny

print(count)