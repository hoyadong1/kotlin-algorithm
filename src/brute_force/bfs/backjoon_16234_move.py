from collections import deque

N, L, R = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

def bfs(x, y, visited):
  q = deque([(x,y)])
  visited[x][y] = True

  union = [(x, y)]
  total = Map[x][y]

  while q:
    x, y = q.popleft()

    for d in range(4):
      nx, ny = x + dx[d], y + dy[d]
      if (0 <= nx < N and 0 <= ny < N):
        if(L <= abs(Map[x][y] - Map[nx][ny]) <= R and not visited[nx][ny]):
          union.append((nx, ny))
          total += Map[nx][ny]
          q.append((nx, ny))
          visited[nx][ny] = True

  return union, total




while True:
  move = False
  visited = [[False] * N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        u ,t = bfs(i, j, visited)

        if len(u) > 1:
          move = True
          avg = t // len(u)

          for x, y in u:
            Map[x][y] = avg

  if not move:
    break

  cnt += 1

print(cnt)

