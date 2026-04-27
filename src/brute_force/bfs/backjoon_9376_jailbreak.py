from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(sx, sy):
    dist = [[-1] * (w + 2) for _ in range(h + 2)]
    dq = deque()
    dq.append((sx, sy))
    dist[sx][sy] = 0

    while dq:
        x, y = dq.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if dist[nx][ny] != -1:
                    continue
                if prison[nx][ny] == '*':
                    continue

                if prison[nx][ny] == '#':
                    dist[nx][ny] = dist[x][y] + 1
                    dq.append((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y]
                    dq.appendleft((nx, ny))

    return dist


t = int(input())

for _ in range(t):
    h, w = map(int, input().split())

    prison = []
    prison.append(['.'] * (w + 2))

    prisoners = []

    for i in range(h):
        row = list(input().strip())
        new_row = ['.'] + row + ['.']
        prison.append(new_row)

        for j in range(w):
            if row[j] == '$':
                prisoners.append((i + 1, j + 1))

    prison.append(['.'] * (w + 2))

    d0 = bfs(0, 0)
    d1 = bfs(prisoners[0][0], prisoners[0][1])
    d2 = bfs(prisoners[1][0], prisoners[1][1])

    ans = float('inf')

    for i in range(h + 2):
        for j in range(w + 2):
            if prison[i][j] == '*':
                continue

            if d0[i][j] == -1 or d1[i][j] == -1 or d2[i][j] == -1:
                continue

            total = d0[i][j] + d1[i][j] + d2[i][j]

            if prison[i][j] == '#':
                total -= 2

            ans = min(ans, total)

    print(ans)