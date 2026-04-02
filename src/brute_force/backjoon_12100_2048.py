N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

answer = 0

def move(m, d):
  new = [[0] * N for _ in range(N)]

  for i in range(N):
    temp = []

    for j in range(N):
        if d == 0:
            val = m[i][j]
        elif d == 1:
            val = m[i][N-1-j]
        elif d == 2:
            val = m[j][i]
        else:
            val = m[N-1-j][i]

        if val != 0:
            temp.append(val)

    merged = []
    idx = 0

    while idx < len(temp):
      if idx + 1 < len(temp) and temp[idx] == temp[idx + 1]:
        merged.append(temp[idx]*2)
        idx+=2
      else:
        merged.append(temp[idx])
        idx +=1

    for j in range(len(merged)):
      if dir == 0:
          new[i][j] = merged[j]
      elif dir == 1:
          new[i][N-1-j] = merged[j]
      elif dir == 2:
          new[j][i] = merged[j]
      else:
          new[N-1-j][i] = merged[j]

  return new

def dfs(m, depth):
  global answer

  if depth >= 5:
    answer = max(answer, max(map(max, m)))
    return

  for d in range(4):
    nm = move(m, d)
    dfs(nm, depth + 1)


dfs(Map, 0)
print(answer)