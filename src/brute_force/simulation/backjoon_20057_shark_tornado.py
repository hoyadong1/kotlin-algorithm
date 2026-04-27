N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

send = [
  (-1, 1, 1), (1, 1, 1),
  (-1, 0, 7), (1, 0, 7),
  (-1, -1, 10), (1, -1, 10),
  (-2, 0, 2), (2, 0, 2),
  (0, -2, 5)
]

def rotate(pattern):
  return [(-y, x, p) for x, y, p in pattern]

patterns = [send]

for _ in range(3):
  patterns.append(rotate(patterns[-1]))

x = y = N // 2
answer = 0

def spread(x, y, d):
  global answer
  total = Map[x][y]
  remain = total
  Map[x][y] = 0

  for dxx, dyy, p in patterns[d]:
    nx, ny = x + dxx, y + dyy
    amount = (total * p) // 100
    remain -= amount

    if 0 <= nx < N and 0 <= ny < N:
      Map[nx][ny] += amount
    else:
      answer += amount
    
  nx, ny = x + dx[d], y + dy[d]
  if 0 <= nx < N and 0 <= ny < N:
    Map[nx][ny] += remain
  else:
    answer += remain

d = 0
move = 1

while True:
  for _ in range(2):
    for i in range(move):
      nx, ny = x + dx[d], y + dy[d]

      spread(nx, ny, d)

      x, y = nx, ny
      if x == 0 and y == 0:
        print(answer)
        exit()
      
    d = (d+1) %4
  move += 1