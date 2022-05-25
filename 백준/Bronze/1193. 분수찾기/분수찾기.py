#1193
n = int(input())

line = 0 # 라인을 늘려감 짝수인지 홀수 인지 1라인은 1개 2라인은 2개요소 3라인은 3개요소임.즉 라인숫자에따라 1+2+3 이렇게 늘어남. 
end = 0 # 그 라인의 끝번호 
while n > end: 
    line += 1  
    end += line 

diff = end - n #내가 찾으려는 몇번째 숫자가 라인의 끝과 얼마나 차이나는지

if line%2 == 0: #짝수 라인 일때는 분모는 1부터 오름차순, 분자는 라인수부터 내림차순 
    top = line - diff 
    bottom = diff + 1 
else:
    top = diff + 1  
    bottom = line - diff 

print("%d/%d"%(top,bottom))