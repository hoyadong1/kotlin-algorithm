from collections import deque

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input().strip())) for _ in range(100)]

    sx, sy = 0, 0
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                sx, sy = i, j

    q = deque()
    q.append((sx, sy))
    visited = [[False] * 100 for _ in range(100)]
    visited[sx][sy] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    ans = 0

    while q:
        x, y = q.popleft()
        if maze[x][y] == 3:
            ans = 1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 100 and 0 <= ny < 100:
                if not visited[nx][ny] and maze[nx][ny] != 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    print(f"#{tc} {ans}")