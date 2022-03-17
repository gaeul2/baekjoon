while True:
    A, B = input().split()
    A = int(A)
    B = int(B)
    if (1 > A or A > 10000) or (1 > B or B > 10000):
        print('1~10000 사이의 수를 입력해주세요')
    else:
        break  
print(A+B)
print(A-B)
print(A*B)
print(int(A/B))
print(A%B)