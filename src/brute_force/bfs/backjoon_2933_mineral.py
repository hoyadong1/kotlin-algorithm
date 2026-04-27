import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
N = int(input())
heights = list(map(int, input().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def throw(height, turn):
    r = R - height
    if turn % 2 == 0:
        for c in range(C):
            if board[r][c] == 'x':
                board[r][c] = '.'
                return
    else:
        for c in range(C - 1, -1, -1):
            if board[r][c] == 'x':
                board[r][c] = '.'
                return


def bfs_ground():
    visited = [[False] * C for _ in range(R)]
    q = deque()

    for c in range(C):
        if board[R - 1][c] == 'x':
            visited[R - 1][c] = True
            q.append((R - 1, c))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if not visited[nx][ny] and board[nx][ny] == 'x':
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return visited


def drop_cluster(visited):
    cluster = []

    for i in range(R):
        for j in range(C):
            if board[i][j] == 'x' and not visited[i][j]:
                cluster.append((i, j))

    if not cluster:
        return

    cluster_set = set(cluster)

    fall = R

    for x, y in cluster:
        nx = x + 1
        dist = 0

        while nx < R:
            if board[nx][y] == 'x' and (nx, y) not in cluster_set:
                break
            nx += 1
            dist += 1

        fall = min(fall, dist)

    for x, y in cluster:
        board[x][y] = '.'

    for x, y in cluster:
        board[x + fall][y] = 'x'


for t in range(N):
    throw(heights[t], t)
    visited = bfs_ground()
    drop_cluster(visited)

for row in board:
    print("".join(row))