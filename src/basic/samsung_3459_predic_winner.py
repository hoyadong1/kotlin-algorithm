T = int(input()) + 1

for tc in range(1,T):
    N = int(input())
    winner = 'Alice'
    
    while N > 3:
        N = N // 2 + 1
        N = N // 2 - 1

    if N == 1:
        winner = 'Bob'
        
    print(f"#{tc} {winner}")