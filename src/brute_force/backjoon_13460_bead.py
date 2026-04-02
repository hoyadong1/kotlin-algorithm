from collections import deque

N, M = map(int, input().split())
Map = [list(input().strip()) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if Map[i][j] == 'R':
            rx, ry = i, j
        elif Map[i][j] == 'B':
            bx, by = i, j

def move(x, y, dx, dy):
  cnt = 0
  while Map[x+dx][y+dy] != '#' and Map[x][y] != "O":
    x += dx
    y += dy
    cnt +=1

  return x, y, cnt


visited = set()
q = deque()
q.append((rx, ry, bx, by, 0))
visited.add((rx, ry, bx, by))

while q:
    rx, ry, bx, by, depth = q.popleft()

    if depth >= 10: break

    for d in range(4):
        nrx, nry, rc = move(rx, ry, dx[d], dy[d])
        nbx, nby, bc = move(bx, by, dx[d], dy[d])

        if Map[nbx][nby] == "O": continue

        if Map[nrx][nry] == "O":
            print(depth + 1)
            exit()
        
        if nrx == nbx and nry == nby:
            if rc > bc:
                nrx -= dx[d]
                nry -= dy[d]
            else:
                nbx -= dx[d]
                nby -= dy[d]

        if (nrx, nry, nbx, nby) not in visited:
          visited.add((nrx, nry, nbx, nby))
          q.append((nrx, nry, nbx, nby, depth + 1))

print(-1)