import sys

for _ in range(int(input())):
    a = list(map(int,sys.stdin.readline().split()))
    avg = sum(a[1:]) // a[0]
    student = 0
    for i in range(1, len(a)):
        if a[i] > avg:
            student += 1

    print(f"{student/a[0] * 100:.3f}"+"%")