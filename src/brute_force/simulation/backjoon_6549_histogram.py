while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    n = arr[0]
    heights = arr[1:]

    stack = []
    max_area = 0

    for i in range(n):
        start = i

        while stack and stack[-1][1] > heights[i]:
            idx, h = stack.pop()
            max_area = max(max_area, h * (i - idx))
            start = idx

        stack.append((start, heights[i]))

    for idx, h in stack:
        max_area = max(max_area, h * (n - idx))

    print(max_area)