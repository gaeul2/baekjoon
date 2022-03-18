num = int(input())
check = num #나중에 원래 숫자와 같은지 확인용
count = 0
while True:
    a = num // 10 #10으로 나눈 몫이 첫째자리수
    b = num % 10 #10으로 나눈 나머지가 두번째 자리수
    c = (a+b)%10 
    num = (b *10) + c
    count += 1
    
    if num == check:
        break
print(count)
