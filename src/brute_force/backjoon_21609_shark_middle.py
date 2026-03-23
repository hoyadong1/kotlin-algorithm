from collections import deque

N, M = map(int, input().split())

Map = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def bfs(x, y, color, visited):
  q = deque([(x, y)])
  blocks = [(x, y)]
  rainbow = []

  visited[x][y] = True
  cnt = 1
  rainbow_cnt = 0

  while q:
    x, y = q.popleft()

    for d in range(4):
      nx, ny = x + dx[d], y + dy[d]

      if 0 <= nx < N and 0 <= ny < N:
        if not visited[nx][ny]:
          if Map[nx][ny] == color:
            visited[nx][ny] = True
            q.append((nx, ny))
            blocks.append((nx, ny))
            cnt += 1
          
          elif Map[nx][ny] == 0:
            visited[nx][ny] = True
            q.append((nx, ny))
            blocks.append((nx, ny))
            rainbow.append((nx, ny))
            cnt += 1
            rainbow_cnt +=1

  for rx, ry in rainbow:
    visited[rx][ry] = False

  return cnt, rainbow_cnt, blocks

def find_group():
  visited = [[False]*N for _ in range(N)]
  groups = []

  for i in range(N):
    for j in range(N):
      if Map[i][j] > 0 and not visited[i][j]:
        cnt, rainbow_cnt, blocks = bfs(i, j, Map[i][j], visited)

        if cnt >= 2:
          normals = [(x, y) for x, y in blocks if Map[x][y] > 0]
          normals.sort()
          sx, sy = normals[0]

          groups.append((cnt, rainbow_cnt, sx, sy, blocks))

  if not groups:
    return None
  
  groups.sort(key = lambda x : (-x[0], -x[1], -x[2], -x[3]))
  return groups[0]

def gravity():
  global Map
  for j in range(N):
    for i in range(N-2, -1, -1):
      if Map[i][j] >= 0:
        r = i
        while True:
          if 0 <= r+1 < N and Map[r+1][j] == -2:
            Map[r+1][j] = Map[r][j]
            Map[r][j] = -2
            r +=1
          else:
            break


def rotate():
    global Map
    new = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new[N-1-j][i] = Map[i][j]
    Map = new
    

score = 0

while True:
  group = find_group()

  if group is None:
    break

  cnt, _, _, _, blocks = group

  for x, y in blocks:
    Map[x][y] = -2

  score += cnt * cnt

  gravity()
  rotate()
  gravity()

print(score)
      


