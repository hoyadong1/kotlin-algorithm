import sys
from collections import deque

input = sys.stdin.readline

def bfs(sy, sx):
    dist = [[-1] * w for _ in range(h)]
    q = deque()
    q.append((sy, sx))
    dist[sy][sx] = 0

    while q:
        y, x = q.popleft()
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w:
                if dist[ny][nx] == -1 and room[ny][nx] != 'x':
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
    return dist


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    room = []
    points = []

    for i in range(h):
        row = list(input().strip())
        room.append(row)
        for j in range(w):
            if row[j] == 'o':
                points.insert(0, (i, j))
            elif row[j] == '*':
                points.append((i, j))

    n = len(points)

    d = [[0]*n for _ in range(n)]

    for i in range(n):
        dist_map = bfs(points[i][0], points[i][1])
        for j in range(n):
            d[i][j] = dist_map[points[j][0]][points[j][1]]

    ok = True
    for i in range(n):
        for j in range(n):
            if d[i][j] == -1:
                ok = False
    if not ok:
        print(-1)
        continue

    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]

    dp[1][0] = 0

    for mask in range(1 << n):
        for i in range(n):
            if dp[mask][i] == INF:
                continue
            for j in range(1, n):
                if not (mask & (1 << j)):
                    nxt = mask | (1 << j)
                    dp[nxt][j] = min(dp[nxt][j], dp[mask][i] + d[i][j])

    ans = min(dp[(1 << n) - 1][i] for i in range(n))
    print(ans)