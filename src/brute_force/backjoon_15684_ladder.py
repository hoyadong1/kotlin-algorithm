N, M, H = map(int, input().split())

line = [[0] * (N) for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    line[a - 1][b - 1] = 1
    line[a - 1][b] = 2


def check():
    same = 0
    for s in range(N):
        now = s
        for j in range(H):
            if line[j][now] == 1:
                now += 1
            elif line[j][now] == 2:
                now -= 1
        if now == s:
            same += 1
    return same


def dfs(n):
    global answer

    if answer != -1:
        return

    temp = check()
    if temp + (cnt - n) * 2 < N:
        return

    if n == cnt:
        if temp == N:
            answer = cnt
        return

    for i in range(H):
        for j in range(N - 1):
            if line[i][j] or line[i][j + 1]:
                continue
            line[i][j], line[i][j + 1] = 1, 2
            dfs(n + 1)
            line[i][j], line[i][j + 1] = 0, 0


answer = -1
for cnt in range(4):
    dfs(0)
    if answer != -1:
        break

print(answer)
