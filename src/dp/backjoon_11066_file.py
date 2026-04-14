T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    prefix = [0] * (K + 1)
    for i in range(K):
        prefix[i+1] = prefix[i] + files[i]

    dp = [[0] * K for _ in range(K)]

    for length in range(2, K+1):
        for i in range(K - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + (prefix[j+1] - prefix[i])
                dp[i][j] = min(dp[i][j], cost)

    print(dp[0][K-1])