T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    points = list(map(int, input().split()))

    cp_x, cp_y = points[0], points[1]
    home_x, home_y = points[2], points[3]

    visited = [False] * N
    min_dist = float('inf')

    def dfs(x, y, cnt, dist):
        global min_dist

        if dist >= min_dist:
            return

        if cnt == N:
            dist += abs(home_x - x) + abs(home_y - y)
            min_dist = min(min_dist, dist)
            return

        for i in range(N):
            if not visited[i]:
                next_x = points[4 + i * 2]
                next_y = points[5 + i * 2]

                next_dist = dist + abs(next_x - x) + abs(next_y - y)

                visited[i] = True
                dfs(next_x, next_y, cnt + 1, next_dist)
                visited[i] = False

    dfs(cp_x, cp_y, 0, 0)
    print(f"#{test_case} {min_dist}")