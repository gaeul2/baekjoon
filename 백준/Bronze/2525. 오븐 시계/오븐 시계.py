#2525
H, M = map(int, input().split())
C = int(input())

def time_car(H,M,C):
    if C < 60:
        if H < 23:
            if H + up_and_down(M,C)[0] > 23:
                H = H + up_and_down(M,C)[0] -24
                print(H, up_and_down(M,C)[1])
            else:
                print(H + up_and_down(M,C)[0], up_and_down(M,C)[1])
        elif H == 23:
            if up_and_down(M,C)[0] == 0:
                print(H, up_and_down(M,C)[1])
            else:
                print(0, up_and_down(M,C)[1])
    elif C >= 60:
        num = C // 60
        C = C % 60
        if H < 23:
            if H + num + up_and_down(M,C)[0] > 23:
                H = H + num + up_and_down(M,C)[0] -24
                print(H, up_and_down(M,C)[1])
            else:
                print(H + num + up_and_down(M,C)[0], up_and_down(M,C)[1])
        elif H == 23:
            if up_and_down(M,C)[0] == 0:
                if H + num <= 23:
                    print(H + num, up_and_down(M,C)[1])
                else:
                    H = H + num -23
                    print(H, up_and_down(M,C)[1])
            else:
                if H + num + up_and_down(M,C)[0] > 23:
                    H = H + num + up_and_down(M,C)[0] -24
                    print(H, up_and_down(M,C)[1])
                else:
                    print(H + num + up_and_down(M,C)[0], up_and_down(M,C)[1])

def up_and_down(M,C):
    num = 0
    minute = 0
    if M + C < 60:
        minute = M+C
        return num, minute
    elif M+ C == 60:
        return num+1, minute
    else: #M+C>60
        minute = abs(60-M-C)

        return num+1, minute

        
time_car(H,M,C)