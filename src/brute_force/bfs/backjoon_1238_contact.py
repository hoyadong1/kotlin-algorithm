from collections import defaultdict, deque

for test_case in range(1, 11):
    length, start = map(int, input().split())
    data = list(map(int, input().split()))

    graph = defaultdict(list)

    for i in range(0, length, 2):
        a = data[i]
        b = data[i + 1]
        graph[a].append(b)

    visited = [False] * 101

    q = deque()
    q.append(start)
    visited[start] = True

    answer = start

    while q:
        size = len(q)
        max_num = 0

        for _ in range(size):
            now = q.popleft()

            max_num = max(max_num, now)

            for nxt in graph[now]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)

        answer = max_num

    print(f"#{test_case} {answer}")