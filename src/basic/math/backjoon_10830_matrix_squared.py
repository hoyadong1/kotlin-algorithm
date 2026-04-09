import sys

input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

MOD = 1000


def mul(X, Y):
    n = len(X)
    res = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += X[i][k] * Y[k][j]
            res[i][j] = s % MOD
    return res


def power(mat, exp):
    n = len(mat)

    if exp == 1:
        return [[x % MOD for x in row] for row in mat]

    half = power(mat, exp // 2)
    half_sq = mul(half, half)

    if exp % 2 == 0:
        return half_sq
    else:
        return mul(half_sq, mat)


result = power(A, B)

for row in result:
    print(*row)
