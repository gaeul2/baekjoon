n = int(input())
ctn = 0

while True:
    if n % 5 == 0: #5kg짜리로 다 담는게 제일 최고의 시나리오 
        ctn += (n // 5) #// 나눗셈의 몫
        print(ctn)#ctn은 여기에 최초로 당도했다면 0인상태이고, 최초가 아니라면 여기를 들어온순간 3만큼씩 빠진횟수만큼 1씩 더해져있음 
        break
    n -= 3 #3만큼 뺐으니
    ctn += 1 #ctn에 1올림(3짜리 봉지에 담은것)
    if n < 0:
        print(-1)
        break