N = int(input()) #처음 숫자를 입력받고 N으로 변수지정
cnt = N #어짜피 입력한 수가 입력받을 단어수와 같으므로 이친구를 카운수로 지정 여기서 오류생길때마다 -1차감

for i in range(N): # 처음 숫자입력받은만큼 반복문돌리고
    word = input() # 그만큼 단어입력받게만듦.
    for j in range(0, len(word)-1): # 공백으로 구분하니까 공백은 세지않도록 범위를 len(word)-1
        if word[j] == word[j+1]: #지금알파벳과 다음알파벳이 같으면 패스
            pass
        elif word[j] in word[j+1:]: #지금알파벳이 다음알파벳이후에 있으면
            cnt -= 1 #1차감
            break # 그리고 이 반복문은 나가고 더 바깥 반복문으로 튕겨냄
print(cnt)
        