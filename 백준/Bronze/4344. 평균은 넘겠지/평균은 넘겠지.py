num = int(input())
for _ in range(num):
    while True:
        scores = list(map(int, input().split()))
        if scores[0] == len(scores[1:]):
            avg = sum(scores[1:])/scores[0] 
                
            cnt = 0
            for i in scores[1:]:
                if i > avg:
                    cnt += 1
            rate= cnt/scores[0]*100
            print(f'{rate:.3f}%')
            break
        else:
            print('입력한 점수의 개수가 학생수와 일치하지 않습니다. 다시입력해주세요')