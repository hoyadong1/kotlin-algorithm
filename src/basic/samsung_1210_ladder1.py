for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    x = 99
    y = ladder[99].index(2)

    while x > 0:
        if y > 0 and ladder[x][y - 1] == 1:
            while y > 0 and ladder[x][y - 1] == 1:
                y -= 1

        elif y < 99 and ladder[x][y + 1] == 1:
            while y < 99 and ladder[x][y + 1] == 1:
                y += 1

        x -= 1

    print(f"#{tc} {y}")
