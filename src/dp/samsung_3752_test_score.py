n = int(input())
arr = list(map(int, input().split()))

max_score = sum(arr)

dp = [False] * (max_score + 1)
dp[0] = True

for s in arr:
    for i in range(max_score, -1, -1):
        if dp[i]:
            dp[i + s] = True

print(sum(dp))