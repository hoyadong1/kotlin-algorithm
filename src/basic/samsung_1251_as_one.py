T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))

    E = float(input())

    visited = [False] * n
    min_dist = [float('inf')] * n

    min_dist[0] = 0
    total = 0

    for _ in range(n):
        u = -1
        min_value = float('inf')

        for i in range(n):
            if not visited[i] and min_dist[i] < min_value:
                min_value = min_dist[i]
                u = i

        visited[u] = True
        total += min_value

        for v in range(n):
            if not visited[v]:
                dx = xs[u] - xs[v]
                dy = ys[u] - ys[v]

                cost = dx * dx + dy * dy

                if cost < min_dist[v]:
                    min_dist[v] = cost

    answer = round(total * E)

    print(f"#{tc} {answer}")