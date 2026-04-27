from collections import deque

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

sx, sy = 0, 0

for i in range(N):
  for j in range(N):
    if Map[i][j] == 9:
      sx, sy = i, j
      Map[i][j] = 0

def bfs(sx, sy, size):
  visited = [[-1] * N for _ in range(N)]
  q = deque()
  q.append((sx, sy))
  visited[sx][sy] = 0
  fishes = []

  while q:
    x, y = q.popleft()

    for d in range(4):
      nx, ny = x + dx[d], y + dy[d]

      if 0 <= nx < N and 0 <= ny < N:
        if visited[nx][ny] == -1 and Map[nx][ny] <= size:
          q.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1

          if 0 < Map[nx][ny] < size:
            fishes.append((visited[nx][ny], nx, ny))

  if not fishes:
    return None
  
  fishes.sort()
  return fishes[0]


size = 2
eat = 0
time = 0

while True:
  result = bfs(sx, sy, size)

  if result == None:
    break

  dist, x, y = result

  time += dist
  eat += 1

  if eat == size:
    size += 1
    eat = 0

  sx, sy = x, y
  Map[sx][sy] = 0


print(time)

