from collections import defaultdict

N, M, K = map(int, input().split())

fireballs = []

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(M):
  r, c, m, s, d = map(int, input().split())
  fireballs.append((r-1, c-1, m, s, d))

for _ in range(K):
  Map = defaultdict(list)

  for x, y, m, s, d in fireballs:
    nx = (x + dx[d]*s) % N
    ny = (y + dy[d]*s) % N
    Map[(nx, ny)].append((m, s, d))

  new = []

  for (x, y), arr in Map.items():
    if len(arr) == 1:
      new.append((x, y, arr[0][0], arr[0][1], arr[0][2]))
      continue

    cnt = len(arr)
    m_sum = 0
    s_sum = 0

    for a in arr:
      m_sum += a[0]
      s_sum += a[1]

    new_m = m_sum // 5
    if new_m == 0:
      continue
    new_s = s_sum // cnt

    even = True
    odd = True

    for a in arr:
      if a[2] % 2 == 0:
        odd = False
      else:
        even = False

    if odd or even:
      dirs = [0, 2, 4, 6]
    else:
      dirs = [1, 3, 5, 7]
    
    for d in dirs:
      new.append((x, y, new_m, new_s, d))
  fireballs = new

answer = sum(x[2] for x in fireballs)
print(answer)

  