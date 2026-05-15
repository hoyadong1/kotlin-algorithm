from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    visited = [False] * (N+1)
    ans = 0

    for i in range(1, N + 1):
        if not visited[i]:
            ans += 1

            q = deque()
            q.append(i)
            visited[i] = True

            while q:
                now = q.popleft()

                for nxt in graph[now]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)

    print(f"#{tc} {ans}")