N, M, K = map(int, input().split())

Map = [list(map(int, input().split())) for _ in range(N)]
dirs = [x-1 for x in map(int, input().split())]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

priority = [[] for _ in range(M)]
for i in range(M):
  for _ in range(4):
    priority[i].append([x-1 for x in map(int, input().split())])


smell = [[[0, 0] for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if Map[i][j] != 0:
            smell[i][j] = [Map[i][j], K]

def move():
  new = [[0]*N for _ in range(N)]

  for i in range(N):
      for j in range(N):
          if Map[i][j] != 0:
            num = Map[i][j]
            d = dirs[num-1]

            empty_found = False

            for nd in priority[num-1][d]:
               nx, ny = i + dx[nd], j + dy[nd]

               if 0 <= nx < N and 0 <= ny < N:
                  if smell[nx][ny][1] == 0:
                     empty_found = True
                     dirs[num-1] = nd

                     if new[nx][ny] == 0 or new[nx][ny] > num:
                      new[nx][ny] = num

                     break
            
            if empty_found:
               continue
            
            for nd in priority[num-1][d]:
              nx, ny = i + dx[nd], j + dy[nd]
              if 0 <= nx < N and 0 <= ny < N:
                if smell[nx][ny][0] == num:
                    dirs[num-1] = nd
                    if new[nx][ny] == 0 or new[nx][ny] > num:
                      new[nx][ny] = num
                    break
  return new


def update_smells():
   for i in range(N):
      for j in range(N):
         if smell[i][j][1] > 0:
            smell[i][j][1] -= 1

         if Map[i][j] != 0:
            smell[i][j] = [Map[i][j], K]


time = 0

while time < 1000:
   time += 1

   Map = move()
   update_smells()

   cnt = 0
   for i in range(N):
      for j in range(N):
         if Map[i][j] != 0:
            cnt += 1

    
   if cnt == 1:
      print(time)
      break
   
else:
   print(-1)