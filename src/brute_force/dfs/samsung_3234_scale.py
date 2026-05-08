T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    weights = list(map(int, input().split()))

    ans = 0
    visited = [False] * N

    total = sum(weights)

    perm = [1] * (N + 1)
    for i in range(1, N + 1):
        perm[i] = perm[i - 1] * i

    def dfs(idx, left, right, remain):
        global ans

        if left < right:
            return

        if idx == N:
            ans += 1
            return

        if left >= right + remain:
            k = N - idx
            ans += perm[k] * (1 << k)
            return

        for i in range(N):
            if not visited[i]:
                visited[i] = True

                dfs(idx + 1, left + weights[i], right, remain - weights[i])
                dfs(idx + 1, left, right + weights[i], remain - weights[i])
                
                visited[i] = False

    dfs(0, 0, 0, total)

    print(f"#{tc} {ans}")