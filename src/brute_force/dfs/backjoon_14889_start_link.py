N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

min_diff = float('inf')
members = [False] * N

def dfs(depth, start):
  global min_diff

  if depth >= N // 2:
    team1 = []
    team2 = []

    sum1 = sum2 = 0

    for i in range(N):
      if members[i]:
        team1.append(i)
      else:
        team2.append(i)

    for i in range(N // 2):
      for j in range(i + 1, N // 2):
        sum1 += (table[team1[i]][team1[j]] + table[team1[j]][team1[i]])
        sum2 += (table[team2[i]][team2[j]] + table[team2[j]][team2[i]])

    min_diff = min(min_diff, abs(sum1 - sum2))
    return

  for i in range(start, N):
    members[i] = True
    dfs(depth + 1, i + 1)
    members[i] = False

dfs(0, 0)
print(min_diff)