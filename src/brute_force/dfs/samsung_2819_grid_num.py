T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, path):
    if len(path) == 7:
        result.add(path)
        return
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, path + board[nx][ny])

for tc in range(1, T + 1):
    board = [input().split() for _ in range(4)]
    
    result = set()
    
    for i in range(4):
        for j in range(4):
            dfs(i, j, board[i][j])
    
    print(f"#{tc} {len(result)}")