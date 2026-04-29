dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] == board[x][y] + 1:
                dp[x][y] = dfs(nx, ny) + 1
                break

    return dp[x][y]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dp = [[-1] * N for _ in range(N)]

    best_len = 0
    best_start = 10**9

    for i in range(N):
        for j in range(N):
            length = dfs(i, j)

            if length > best_len:
                best_len = length
                best_start = board[i][j]
            elif length == best_len:
                best_start = min(best_start, board[i][j])

    print(f"#{tc} {best_start} {best_len}")