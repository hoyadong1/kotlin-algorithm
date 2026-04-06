import sys
import heapq

input = sys.stdin.readline

left = []
right = []

N = int(input())

for _ in range(N):
    x = int(input())

    heapq.heappush(left, -x)

    if right and -left[0] > right[0]:
        val = -heapq.heappop(left)
        heapq.heappush(right, val)

    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))

    print(-left[0])