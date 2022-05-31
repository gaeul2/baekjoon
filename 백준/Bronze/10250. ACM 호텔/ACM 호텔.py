N = int(input())

f = 0
ho = 0
for _ in range(N):
    h, w, n = map(int, input().split())
    if n % h == 0:
        f = h * 100
        ho = n // h
    else:
        f = (n % h) * 100 # 400
        ho = n // h + 1
    print(f + ho)