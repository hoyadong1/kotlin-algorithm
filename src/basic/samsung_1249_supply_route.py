import heapq

T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for test_case in range(1, T + 1):
    N = int(input())

    cmap = [list(map(int, input().strip())) for _ in range(N)]
    dist = [[float('inf')] * N for _ in range(N)]
    pq = []

    dist[0][0] = 0
    heapq.heappush(pq, (0, 0, 0))

    while pq:
        cost, x, y = heapq.heappop(pq)

        if dist[x][y] < cost:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:

                ncost = cost + cmap[nx][ny]

                if ncost < dist[nx][ny]:
                    dist[nx][ny] = ncost
                    heapq.heappush(pq, (ncost, nx, ny))

    print(f"#{test_case} {dist[N-1][N-1]}")