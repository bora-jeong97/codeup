'''파이썬의 자료형'''
'''
기본 데이터 형식
    리터럴 : 상수
    불   : True False
    숫자형
        정수(int)
        실수(float)
연속형 데이터 형식
    가변형
        배열(리스트) : 리스트 이름 = []
        딕셔너리
        세트
    불변형  
        문자열
        튜플      

'''

# 리스트
aa = [10, 20 , 30 , 40]
aa.append(0)
print(aa)
print(len(aa))
print(aa[3])

# 리스트 접근법
print(aa[0:3])
print(aa[:2])
print(aa[2:])


# 유용한 리스트 함수들
bb = [10, 20, 30]
bb.append(40)
bb.append(40)
print(bb)
bb.pop()
print(bb)
bb.sort() # 오름차순
print(bb)
bb.reverse()    # 내림차순
print(bb)
bb.insert(0, 33) # 해당 index에 끼워넣기
print(bb)
bb.extend([50, 60, 70]) # 합치기
print(bb)
print(bb.count(10)) # 해당값이 몇개인지 세기
print(bb.index(50)) # 인덱스 찾기

'''  2차원 리스트  '''
list1 = []  # 행
list2 = []  # 열
value = 1

# 입력
for i in range(0, 3):   # 3행 4열
    for j in range(0, 4):
        list1.append(value) # [5, 6, 7, 8]
        value += 1
    list2.append(list1)
    list1 = []  # 다시 행을 넣을 수 있도록 비워준다
# 출력
for i in range(0, 3):   # 3행 4열
    for j in range(0, 4):
        print(f"{list2[i][j]}", end=" ")
    print("")


''' 컴프리헨션(Comprehension, 함축) 
리스트 = [수식 for 항목 in range() if 조건식]
'''
# 1차원 리스트
numlist = []
for num in range(1, 6):
    numlist.append(num)
print(numlist)

numlist = [num for num in range(1, 6)]
print(numlist)


numlist = [num*num for num in range(1, 6)]
print(numlist)

numlist = [num for num in range(1, 31) if num % 2 == 0]
print(numlist)

# 2차원 리스트의 컴프리헨션
list2 = [[0 for _ in range(3)] for _ in range(4)]
print(list2)

''' 다중 인덱스 반환
print([i for i, value in enumerate(data) if value == 1])
enumerate : 인덱스와 값을 반환함
'''
mutiIndex = [i for i,v in enumerate(numlist) if (v == 10) or (v == 4)]
print(mutiIndex)

