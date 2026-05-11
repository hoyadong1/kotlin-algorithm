from collections import deque

pair = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<'
}

for tc in range(1, 11):
    n = int(input())
    arr = list(input().strip())

    st = deque()
    ans = 1

    for c in arr:
        if c in '({[<':
            st.append(c)

        else:
            if not st:
                ans = 0
                break

            top = st.pop()

            if top != pair[c]:
                ans = 0
                break

    if st:
        ans = 0

    print(f"#{tc} {ans}")