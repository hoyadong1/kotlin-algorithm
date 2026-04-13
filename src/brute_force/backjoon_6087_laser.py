from collections import deque

W, H = map(int, input().split())
Map = [list(input().strip()) for _ in range(H)]

CP = []
for i in range(H):
    for j in range(W):
        if Map[i][j] == 'C':
            CP.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

INF = int(1e9)
dist = [[[INF]*4 for _ in range(W)] for _ in range(H)]

sx, sy = CP[0]
ex, ey = CP[1]

dq = deque()

for d in range(4):
    dist[sx][sy][d] = 0
    dq.append((sx, sy, d))

while dq:
    x, y, d = dq.popleft()

    for nd in range(4):
        nx, ny = x + dx[nd], y + dy[nd]

        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if Map[nx][ny] == '*':
            continue

        cost = dist[x][y][d]
        if d != nd:
            cost += 1

        if dist[nx][ny][nd] > cost:
            dist[nx][ny][nd] = cost
            dq.append((nx, ny, nd))

print(min(dist[ex][ey]))