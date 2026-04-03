from itertools import combinations
from collections import deque

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


virus = []
empty = 0

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i, j))
        elif lab[i][j] == 0:
            empty += 1


def bfs(vir):
    q = deque()
    visited = [[-1] * N for _ in range(N)]

    for x, y in vir:
        visited[x][y] = 0
        q.append((x, y))

    filled = 0
    time = 0

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if lab[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

                    if lab[nx][ny] == 0:
                        filled += 1
                        time = visited[nx][ny]

    return time if filled == empty else float("inf")


answer = float("inf")

for comb in combinations(virus, M):
    answer = min(answer, bfs(comb))

print(answer if answer != float("inf") else -1)
