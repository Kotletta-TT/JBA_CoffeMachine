N = int(input())
answer = 1
if 1 <= N <= 100:
    while N:
        answer *= N
        N -= 1
print(answer)