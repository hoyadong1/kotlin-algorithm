from collections import deque

N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

tx, ty = map(int, input().split())
tx -= 1
ty -= 1

passengers = {}
for _ in range(M):
    a, b, c, d = map(int, input().split())
    passengers[(a-1, b-1)] = (c-1, d-1)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def find_passenger():
    visited = [[-1]*N for _ in range(N)]
    q = deque([(tx, ty)])
    visited[tx][ty] = 0

    best = None

    while q:
        x, y = q.popleft()
        d = visited[x][y]

        if best and d > best[0]:
            break

        if (x, y) in passengers:
            if best is None or (d, x, y) < best and d <= fuel:
                best = (d, x, y)
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = d + 1
                    q.append((nx, ny))

    return best

def get_dist(sx, sy, ex, ey):
    visited = [[-1]*N for _ in range(N)]
    q = deque([(sx, sy)])
    visited[sx][sy] = 0

    while q:
        x, y = q.popleft()

        if (x, y) == (ex, ey):
            return visited[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return -1

for _ in range(M):
    res = find_passenger()

    if res is None:
        print(-1)
        exit()

    dist, px, py = res

    if fuel < dist:
        print(-1)
        exit()

    fuel -= dist
    tx, ty = px, py

    ex, ey = passengers[(px, py)]
    passengers.pop((px, py))

    dist2 = get_dist(tx, ty, ex, ey)

    if dist2 == -1 or fuel < dist2:
        print(-1)
        exit()

    fuel -= dist2
    fuel += dist2 * 2

    tx, ty = ex, ey

print(fuel)