T = int(input())

for test_case in range(1, T + 1):
    A = input().strip()
    
    hasN = hasS = hasE = hasW = False
    
    for c in A:
        if c == 'N': hasN = True
        elif c == 'S': hasS = True
        elif c == 'E': hasE = True
        elif c == 'W': hasW = True
    
    vertical = (not hasN and not hasS) or (hasN and hasS)
    horizontal = (not hasE and not hasW) or (hasE and hasW)
    
    print("Yes" if vertical and horizontal else "No")