N = int(input())

recycle = 0
while recycle != N:
    test = input()
    cnt = 0
    sum_list = []
    for i in range(len(test)):
        if test[i] == 'O':
            if cnt >= 1:
                cnt += 1
                sum_list.append(cnt)
            else:
                cnt = 1
                sum_list.append(cnt)
        else:
            cnt = 0
    recycle += 1
    print(sum(sum_list))