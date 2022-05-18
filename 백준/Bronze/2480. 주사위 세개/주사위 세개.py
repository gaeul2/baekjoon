one, two, three = map(int, input().split())

box = [one, two, three]
num = len(set(box))

if num == 1:
    print(10000+(box[0]*1000))
elif num == 3:
    print(max(box) * 100) 
else:
    tmp = box[2]
    box.pop()
    if tmp in box:
        print(1000+(tmp * 100))
    else:
        print(1000 +(box[1]*100))