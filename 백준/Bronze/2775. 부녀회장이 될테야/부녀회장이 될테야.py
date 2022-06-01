lst = [[0 for j in range(14)] for i in range(15)] #층별로 만들고
for i in range(15):
    lst[i][0] = 1 #1호는 다 1임
for h in range(14): #0층은 1씩증가하는 리스트만듬
    lst[0][h] = h + 1
for i in range(1, 15): #층수처럼 1층/2층/3층로 리스트번호
    for j in range(1, 14): #각리스트의 인덱스
        lst[i][j] = lst[i][j-1] + lst[i-1][j] #앞집, 밑집 객체들고옴

N= int(input())

for _ in range(N):
    k = int(input())
    n = int(input())
    print(lst[k][n-1]) #인덱스번호는 0부터 시작하므로