from itertools import combinations
from collections import deque

# 입력 값 처리하기

N, M = map(int, input().split())

Map = [list(map(int, input().split())) for _ in range(N)]

empty = []
virus = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 빈칸 바이러스 위치 파악 후 채우기

for i in range(N):
  for j in range(M):
    if Map[i][j] == 0:
      empty.append((i,j))
    elif Map[i][j] == 2:
      virus.append((i,j))

# 바이러스 퍼트리는 함수 만들기

def bfs(temp):
  q = deque(virus)

  while q:
    x, y = q.popleft()
    for d in range(4):
      nx, ny = x + dx[d], y + dy[d]

      if 0 <= nx < N and 0 <= ny < M:
        if temp[nx][ny] == 0:
          temp[nx][ny] = 2
          q.append((nx, ny))


# 안전구역 세는 함수 만들기

def count_safe(temp):
  cnt = 0
  for i in range(N):
    for j in range(M):
      if temp[i][j] == 0:
        cnt +=1

  return cnt

# 모든 조합에 대해서 벽 세우고 바이러스 터트려보고 카운트 후 맥스 값 출력

answer = 0

for walls in combinations(empty, 3):

  temp = [row[:] for row in Map]

  for x, y in walls:
    temp[x][y] = 1

  bfs(temp)

  result = count_safe(temp)

  answer = max(answer, result)

print(answer)