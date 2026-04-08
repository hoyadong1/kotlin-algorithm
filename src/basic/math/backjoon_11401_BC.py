import sys
input = sys.stdin.readline

N, K = map(int, input().split())

MOD = 1000000007

def power(a, b):
    res = 1
    a %= MOD

    while b > 0:
        if b % 2 == 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b //= 2

    return res

fact = [1] * (N + 1)

for i in range(1, N + 1):
    fact[i] = (fact[i - 1] * i) % MOD


top = fact[N]
bot = (fact[K] * fact[N - K]) % MOD

answer = top * power(bot, MOD - 2) % MOD

print(answer)