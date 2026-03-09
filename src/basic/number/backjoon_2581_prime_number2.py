M = int(input())
N = int(input())

sum = 0
min_val = -1

for i in range(M, N + 1):
    if i == 1:
        continue

    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        sum += i
        if min_val == -1:
            min_val = i

if min_val == -1:
    print(-1)
else:
    print(sum)
    print(min_val)