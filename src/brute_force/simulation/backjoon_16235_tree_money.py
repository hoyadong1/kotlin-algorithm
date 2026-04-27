from collections import defaultdict

N, M, K = map(int, input().split())

land = [[5] * N for _ in range(N)]
add = [list(map(int, input().split())) for _ in range(N)]
trees = [[defaultdict(int) for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1][z] += 1

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(K):

    for i in range(N):
        for j in range(N):
            if not trees[i][j]:
                continue

            new = defaultdict(int)
            dead = 0

            for age in sorted(trees[i][j].keys()):
                cnt = trees[i][j][age]

                can = min(cnt, land[i][j] // age)
                if can > 0:
                    new[age + 1] += can
                    land[i][j] -= can * age

                dead += (cnt - can) * (age // 2)

            land[i][j] += dead
            trees[i][j] = new

    for i in range(N):
        for j in range(N):
            for age, cnt in trees[i][j].items():
                if age % 5 == 0:
                    for d in range(8):
                        nx = i + dx[d]
                        ny = j + dy[d]

                        if 0 <= nx < N and 0 <= ny < N:
                            trees[nx][ny][1] += cnt

    for i in range(N):
        for j in range(N):
            land[i][j] += add[i][j]


answer = 0
for i in range(N):
    for j in range(N):
        answer += sum(trees[i][j].values())

print(answer)
