T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    points = []
 
    min_x = {}
    max_x = {}
    min_y = {}
    max_y = {}
 
    xs = {}
    ys = {}
 
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
 
        if x not in xs:
            xs[x] = []
        if y not in ys:
            ys[y] = []
 
        xs[x].append(y)
        ys[y].append(x)
 
    for x in xs:
        min_y[x] = min(xs[x])
        max_y[x] = max(xs[x])
 
    for y in ys:
        min_x[y] = min(ys[y])
        max_x[y] = max(ys[y])
 
    ans = 0
 
    for x, y in points:
        vert = max(abs(max_y[x] - y), abs(y - min_y[x]))
        hori = max(abs(max_x[y] - x), abs(x - min_x[y]))
        ans = max(ans, vert * hori)
 
    print(ans)