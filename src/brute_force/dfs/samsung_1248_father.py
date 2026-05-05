T = int(input())
for tc in range(1, T+1):
    V, E, A, B = map(int, input().split())
    arr = list(map(int, input().split()))
    
    parent = [0] * (V + 1)
    tree = [[] for _ in range(V + 1)]
    
    for i in range(0, E*2, 2):
        p = arr[i]
        c = arr[i+1]
        parent[c] = p
        tree[p].append(c)
    
    visited = set()
    x = A
    while x:
        visited.add(x)
        x = parent[x]
    
    y = B
    while y:
        if y in visited:
            lca = y
            break
        y = parent[y]

    def dfs(x):
      cnt = 1
      for nx in tree[x]:
          cnt += dfs(nx)
      return cnt
    
    size = dfs(lca)
    
    print(f"#{tc} {lca} {size}")