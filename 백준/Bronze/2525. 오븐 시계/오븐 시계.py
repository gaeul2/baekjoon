def oven_clock(H, M, C):
    M += C
    extra_hour = 0

    H += (M // 60)
    M = (M % 60)

    if H >= 24:
        H -= 24
    print(H, M)

H, M = map(int, input().split())
C = int(input())

oven_clock(H,M,C)