from collections import deque

T = int(input())

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

for tc in range(1, T + 1):
    R, C = map(int, input().split())

    board = [list(input()) for _ in range(R)]

    visited = [[[[False] * 16 for _ in range(4)] for _ in range(C)] for _ in range(R)]

    q = deque()
    q.append((0, 0, 0, 0))

    visited[0][0][0][0] = True

    answer = "NO"

    while q:
        r, c, d, mem = q.popleft()

        cmd = board[r][c]

        if cmd == '@':
            answer = "YES"
            break

        nd = d
        nmem = mem

        if cmd == '>':
            nd = 0

        elif cmd == '<':
            nd = 1

        elif cmd == '^':
            nd = 2

        elif cmd == 'v':
            nd = 3

        elif cmd == '_':
            if mem == 0:
                nd = 0
            else:
                nd = 1

        elif cmd == '|':
            if mem == 0:
                nd = 3
            else:
                nd = 2

        elif cmd == '+':
            nmem = (mem + 1) % 16

        elif cmd == '-':
            nmem = (mem - 1) % 16

        elif cmd.isdigit():
            nmem = int(cmd)

        if cmd == '?':
            for td in range(4):
                nr = (r + dr[td]) % R
                nc = (c + dc[td]) % C

                if not visited[nr][nc][td][nmem]:
                    visited[nr][nc][td][nmem] = True
                    q.append((nr, nc, td, nmem))

        else:
            nr = (r + dr[nd]) % R
            nc = (c + dc[nd]) % C

            if not visited[nr][nc][nd][nmem]:
                visited[nr][nc][nd][nmem] = True
                q.append((nr, nc, nd, nmem))

    print(f"#{tc} {answer}")