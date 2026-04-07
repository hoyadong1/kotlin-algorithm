from collections import deque

R, C = map(int, input().split())
lake = [list(input().strip()) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * C for _ in range(R)]

swans = []
water_q = deque()
swan_q = deque()

day = 0

for i in range(R):
    for j in range(C):
        if lake[i][j] == 'L':
            swans.append((i, j))
        if lake[i][j] != 'X':
            water_q.append((i, j))

def melt():
  next_water_q = deque()

  while water_q:
    x, y = water_q.popleft()

    for d in range(4):
      nx, ny = x + dx[d], y + dy[d]

      if 0 <= nx < R and 0 <= ny < C:
        if lake[nx][ny] == 'X':
          lake[nx][ny] = '.'
          next_water_q.append((nx, ny))

  return next_water_q
  

def move_swan():
    next_swan_q = deque()

    while swan_q:
        x, y = swan_q.popleft()

        if (x, y) == swans[1]:
            print(day)
            exit()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                visited[nx][ny] = True

                if lake[nx][ny] == 'X':
                    next_swan_q.append((nx, ny))
                else:
                    swan_q.append((nx, ny))

    return next_swan_q


swan_q.append(swans[0])
visited[swans[0][0]][swans[0][1]] = True

while True:
    swan_q = move_swan()
    water_q = melt()
    
    day += 1