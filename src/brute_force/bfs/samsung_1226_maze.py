from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for tc in range(1, 11):
    num = int(input())
    board = [list(input().strip()) for _ in range(16)]
    sx = sy = ex = ey = 0
    ans = 0
    
    q = deque()
    visited = [[False] * 16 for _ in range(16)]
    
    for i in range(16):
        for j in range(16):
            if board[i][j] == '2':
                sx, sy = i, j
            if board[i][j] == '3':
                ex, ey = i, j
                
    q.append((sx, sy))
    visited[sx][sy] = True
   
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            ans = 1
            break
        
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            
            if 0 <= nx < 16 and 0 <= ny < 16 and board[nx][ny] != '1' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                
    print(f"#{num} {ans}")