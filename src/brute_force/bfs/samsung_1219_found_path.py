from collections import deque
 
for tc in range(1, 11):
    c, n = map(int, input().split())
    pairs = list(map(int, input().split()))
     
    graph = [[] for _ in range(100)]
     
    for i in range(0, n*2, 2):
        s, e = pairs[i], pairs[i+1]
        graph[s].append(e)
     
    visited = [False] * 100
    q = deque()
    q.append(0)
    visited[0] = True
     
    ans = 0
     
    while q:
        now = q.popleft()
        if now == 99: 
            ans = 1
            break
         
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    print(f"#{tc} {ans}")