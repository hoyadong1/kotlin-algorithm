for i in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0
    
    for j in range(2, N - 2):
        near = max(buildings[j-1], buildings[j-2], buildings[j+1], buildings[j+2])
        if near >= buildings[j]:
            continue
        cnt += buildings[j] - near
    
    print(f"#{i} {cnt}")