num = int(input())
num_list= list(map(int,input().split()))

#진짜 약수가 모두 주어지기때문에
#가장 작은값과 가장큰값을 곱하면 진짜수
max_num = max(num_list)
min_num = min(num_list)

print(max_num*min_num)