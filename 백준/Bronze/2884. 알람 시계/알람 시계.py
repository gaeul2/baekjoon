while True:
    H, M= input().split(" ")
    H = int(H)
    M = int(M)
    if ( H < 0 or H >= 24) and (M < 0 or M >= 60):
        print('H는 0~23사이의 수로, M은 0~59사이의 수로 입력하세요')
    elif (M < 0 or M >= 60) :
        print('M은 0~59사이의 수로 입력하세요')
    elif ( H < 0 or H >= 24):
        print('H는 0~23사이의 수로 입력하세요')
    else:
        H = (H - 1)
        M = (M - 45)
        if M < 0: # M-45가 음수가 될때
            M = M + 60
            if H <= 0: #H-1이 0과 같거나 작을때
                if H == -1:
                    H = 23
                    print(H, M)
                    break
                else:
                    print(H, M)
                    break
            else:
                print(H, M)
                break
        else:
            if M == 0: #M이 0과 같을때
                M = 0
                print(H+1, M)
                break
            else: #M이 0보다 크고 45보다 클때
                if H == -1:
                    print(H+1, M)
                    break
                else:
                    print(H+1, M)
                    break