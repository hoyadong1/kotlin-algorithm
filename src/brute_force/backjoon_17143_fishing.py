R, C, M = map(int, input().split())

sharks = dict()

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1

    sharks[(r, c)] = [s, d, z]


total = 0

for fisher in range(C):

    for i in range(R):
        if (i, fisher) in sharks:
            total += sharks[(i, fisher)][2]
            del sharks[(i, fisher)]
            break

    new_sharks = dict()

    for (x, y), (s, d, z) in sharks.items():

        if d in (0, 1):
            cycle = 2 * (R - 1)
            s %= cycle

            if d == 0:
                pos = x - s
            else:
                pos = x + s

            pos %= cycle

            if pos >= R:
                pos = cycle - pos
                d ^= 1

            nx = pos
            ny = y

        else:
            cycle = 2 * (C - 1)
            s %= cycle

            if d == 3:
                pos = y - s
            else:
                pos = y + s

            pos %= cycle

            if pos >= C:
                pos = cycle - pos
                d ^= 1

            nx = x
            ny = pos

        if (nx, ny) in new_sharks:
            if new_sharks[(nx, ny)][2] < z:
                new_sharks[(nx, ny)] = [s, d, z]
        else:
            new_sharks[(nx, ny)] = [s, d, z]

    sharks = new_sharks


print(total)
