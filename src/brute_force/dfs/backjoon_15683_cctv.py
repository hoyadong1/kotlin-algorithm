# 입력 처리

N, M = map(int, input().split())

Map = [list(map(int, input().split())) for _ in range(N)]

cctv = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dirs = [
  [],
  [[0], [1], [2], [3]],
  [[0, 2], [1, 3]],
  [[0, 1], [1, 2], [2, 3], [3, 0]],
  [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
  [[0, 1, 2, 3]]
]

for i in range(N):
  for j in range(M):
    if 1 <= Map[i][j] <= 5:
      cctv.append((i, j, Map[i][j]))

# 감시 처리 함수

def watch(temp, x, y, direc):
  for d in direc:
    nx, ny = x, y
    while True:
      nx += dx[d]
      ny += dy[d]
      if not (0 <= nx < N and 0 <= ny < M):
        break
      if temp[nx][ny] == 6:
        break
      temp[nx][ny] = -1


# 사각지대 계산 함수

def count_dan(temp):
  cnt = 0
  for i in range(N):
    for j in range(M):
      if temp[i][j] == 0:
        cnt +=1

  return cnt

# 모든 경우의 수 반복 함수

answer = 99999

def dfs(depth, temp):
  global answer

  if depth >= len(cctv):
    result = count_dan(temp)
    answer = min(answer, result)
    return
  
  x, y, t = cctv[depth]

  for direc in dirs[t]:
    new = [row[:] for row in temp]
    watch(new, x, y, direc)
    dfs(depth + 1, new)

dfs(0, Map)
print(answer)