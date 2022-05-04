N = int(input())

for i in range(N):
    reversed_sentence =''
    sentence = input().split()
    for word in sentence:
        reversed_sentence += (word[::-1]+' ')
    print(reversed_sentence)