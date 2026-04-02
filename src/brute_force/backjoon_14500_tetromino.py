N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = [[False]*M for _ in range(N)]

answer = 0

def dfs(x, y, depth, total):
  global answer

  if depth >= 4:
    answer = max(answer, total)
    return
  
  for d in range(4):
    nx, ny = x + dx[d], y + dy[d]

    if 0 <= nx < N and 0 <= ny < M:
      if not visited[nx][ny]:
        visited[nx][ny] = True
        dfs(nx, ny, depth + 1, total + map[nx][ny])
        visited[nx][ny] = False


def chech(x, y):
  global answer
  center = map[x][y]
  sides = []

  for d in range(4):
    nx, ny = x + dx[d], y + dy[d]

    if 0 <= nx < N and 0 <= ny < M:
      sides.append(map[nx][ny])

    if len(sides) >= 3:
      sides.sort(reverse=True)
      answer = max(answer, center + sum(sides[:3]))


for i in range(N):
  for j in range(M):
    visited[i][j] = True
    dfs(i, j, 1, map[i][j])
    visited[i][j] = False

    chech(i, j)

print(answer)