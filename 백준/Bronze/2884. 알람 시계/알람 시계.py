H, M = map(int, input().split())


def chang(H,M):
    min = M -45
    if H == 0:
        if min < 0:
            print(23, min+60)
        elif min == 0:
            print(0, 0)
        else:
            print(0, min)
    else: 
        if min < 0:
            print(H-1, min+60)
        elif min == 0:
            print(H, 0)
        else:
            print(H, min)
   
chang(H,M)