T = int(input())

for test_case in range(1, T + 1):
  N, B = map(int, input().split())
  H = list(map(int, input().split()))

  max_sum = sum(H)

  dp = [False] * (max_sum+1)
  dp[0] = True

  for h in H:
    for s in range(max_sum, -1, -1):
      if dp[s]:
        dp[s + h] = True

  ans = float("inf")

  for s in range(B, max_sum+1):
    if dp[s]:
      ans = s
      break

  print(f"#{test_case} {ans - B}")