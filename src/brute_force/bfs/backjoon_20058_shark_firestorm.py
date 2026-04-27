from collections import deque

N, Q = map(int, input().split())
n = 2**N
Map = [list(map(int, input().split())) for _ in range(n)]
L = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def melt():
  minus = []

  for i in range(n):
    for j in range(n):
      if Map[i][j] == 0:
        continue

      count = 0
      for d in range(4):
        nx, ny = i + dx[d], j + dy[d]
        if 0 <= nx < n and 0 <= ny < n and Map[nx][ny] > 0:
          count += 1

      if count < 3:
        minus.append((i, j))

  for x, y in minus:
    if Map[x][y] > 0:
        Map[x][y] -= 1


def rotate(l):
  m = 2**l
  new = [[0]*n for _ in range(n)]

  for i in range(0, n, m):
    for j in range(0, n, m):
      for x in range(m):
        for y in range(m):
          new[i+y][j+m-1-x] = Map[i+x][j+y]
  return new


def ice_sum():
  total = 0

  for i in range(n):
    for j in range(n):
      total += Map[i][j]
  return total

def bfs(x, y, visited):
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  count = 1

  while q:
    x, y = q.popleft()

    for d in range(4):
      nx, ny = x + dx[d], y + dy[d]

      if 0 <= nx < n and 0 <= ny < n:
        if not visited[nx][ny] and Map[nx][ny] != 0:
          visited[nx][ny] = True
          q.append((nx, ny))
          count += 1

  return count


for l in L:
  Map = rotate(l)
  melt()

big = 0
visited = [[False]*n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if Map[i][j] > 0 and not visited[i][j]:
        big = max(big, bfs(i, j, visited))


print(ice_sum())
print(big)