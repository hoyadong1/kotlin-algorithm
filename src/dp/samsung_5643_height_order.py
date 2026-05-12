T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    M = int(input())

    graph = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            if graph[i][k]:
                for j in range(1, N + 1):
                    if graph[k][j]:
                        graph[i][j] = 1

    ans = 0

    for i in range(1, N + 1):
        cnt = 0

        for j in range(1, N + 1):
            if graph[i][j] or graph[j][i]:
                cnt += 1

        if cnt == N - 1:
            ans += 1

    print(f'#{tc} {ans}')