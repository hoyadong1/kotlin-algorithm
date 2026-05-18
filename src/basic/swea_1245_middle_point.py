T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = list(map(int, input().split()))

    pos = arr[:N]
    mass = arr[N:]

    ans = []

    for i in range(N - 1):

        left = pos[i]
        right = pos[i + 1]

        for _ in range(100):

            mid = (left + right) / 2

            left_force = 0
            right_force = 0

            for j in range(i + 1):
                left_force += mass[j] / ((mid - pos[j]) ** 2)

            for j in range(i + 1, N):
                right_force += mass[j] / ((pos[j] - mid) ** 2)

            if left_force > right_force:
                left = mid
            else:
                right = mid

        ans.append((left + right) / 2)

    print(f"#{tc}", end=' ')
    for x in ans:
        print(f"{x:.10f}", end=' ')
    print()