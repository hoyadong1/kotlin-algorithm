n = int(input())
mod = 1000000
pisano = 1500000

n %= pisano

current = 1
before = 0

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for _ in range(n - 1):
        current, before = (current + before) % mod, current

    print(current)
