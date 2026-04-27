from collections import deque

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

T = int(input())

def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N

for tc in range(1, T+1):
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]
    
    cnt = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                cnt[i][j] = -1
                continue
            c = 0
            for d in range(8):
                ni, nj = i+dx[d], j+dy[d]
                if in_range(ni, nj, N) and board[ni][nj] == '*':
                    c += 1
            cnt[i][j] = c

    visited = [[False]*N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if cnt[i][j] == 0 and not visited[i][j]:
                ans += 1
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                
                while q:
                    x, y = q.popleft()
                    for d in range(8):
                        nx, ny = x+dx[d], y+dy[d]
                        if in_range(nx, ny, N) and not visited[nx][ny] and cnt[nx][ny] != -1:
                            visited[nx][ny] = True
                            if cnt[nx][ny] == 0:
                                q.append((nx, ny))

    for i in range(N):
        for j in range(N):
            if cnt[i][j] != -1 and not visited[i][j]:
                ans += 1

    print(f"#{tc} {ans}")