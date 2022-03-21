from collections import Counter
while True:
    word = list(map(str, input().lower()))
    if len(word) > 1000000 or len(word) <= 0:
        print('1~1000000사이의 길이의 단어를 입력하세요')
    else:
        ctn = Counter(word)
        letter= ctn.most_common(1)
        if len(word) == 1:
            print(word[0].upper())
            break
        elif letter[0][1] == ctn.most_common(2)[1][1]:
            print('?')
            break
        else:
            print(letter[0][0].upper())
            break