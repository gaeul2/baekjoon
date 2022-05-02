numbers = set(range(1, 10001))
remove_set = set() # 비어 있는 집합 자료형은 s = set()로 만들수 있다.
for number in numbers: #11------------------------------------12
    for num in str(number): #1 11 // 1 11-------------------- 1 12 // 2 12
        number += int(num) #11 + 1 // 12 + 1 /// number=13----12+1 // 13+2 // number 15
    remove_set.add(number) # add() : 집합에 요소를 추가할때

self_number = numbers - remove_set # set의 '-' 연산자로 차집합을 구함
#집합은 순서가 없는게 특징이므로 정렬을 해줘야함
for self_num in sorted(self_number):
    print(self_num)