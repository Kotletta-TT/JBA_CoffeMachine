N = int(input())
R = int(input())
T = 0

if 1 < N <= 1000000:
    while N > R:
        N //= 2
        T += 12
    print(T)