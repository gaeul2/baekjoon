m = int(input())
n = int(input())
sosu = []

for i in range(m, n+1):
    error = 0
    if i == 1:
        error = 1
    for j in range(2, i+1):
        if i == j:
            pass
        elif i % j == 0:
            error += 1
            if error >= 1:
                break
    if error == 0:
       sosu.append(i)

if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))
