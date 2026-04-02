N = int(input())
tests = list(map(int, input().split()))
A, B = map(int, input().split())

answer = 0

for t in tests:
  if t - A >0:
    answer += (t-A)//B
    if (t-A)%B != 0:
      answer +=1
  answer +=1

print(answer)


