N = int(input())
students = {}
order = []

for _ in range(N * N):
  data = list(map(int, input().split()))
  students[data[0]] = data[1:]
  order.append(data[0])

Map = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for student in students:
  candy = []

  for i in range(N):
    for j in range(N):
      if Map[i][j] != 0:
        continue

      like = 0
      empty = 0

      for d in range(4):
        nx, ny = i + dx[d], j + dy[d]

        if 0 <= nx < N and 0 <= ny < N:
          if Map[nx][ny] in students[student]:
            like +=1
          if Map[nx][ny] == 0:
            empty += 1

      candy.append((-like, -empty, i, j))

  candy.sort()
  x, y = candy[0][2], candy[0][3]
  Map[x][y] = student

result = 0

for i in range(N):
    for j in range(N):
        cnt = 0

        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if Map[nx][ny] in students[Map[i][j]]:
                    cnt += 1

        if cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000

print(result)