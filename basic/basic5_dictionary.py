'''딕셔너리(가변형 데이터 타입)
딕셔너리변수 = {키:값1, 키2:값2, 키3,값3}
'''
# 초기세팅
student = {'학번':10000, '이름':'홍길동'}
print(student)

# 추가 [키] = 값 형식으로 사용
student['혈액형'] = 'A'
print(student)

# 존재하는 키를 사용하면 기존 값이 변경된다
student['혈액형'] = 'B'
print(student)

# 삭제
del(student['혈액형'])
print(student)

# 키의 유일성, 중복될시 마지막 키가 적용된다
student = {'학번': 10000, '이름': '홍길동', '이름': '나봉순'}
print(student)

# 탐색은 key
print(student['이름'])
print(student.get('이름'))
print(student.keys())
print(student.values())

# 리스트화
print(list(student.keys()))

# 튜플화
print(student.items())
print(list(student.items()))    # dict_items제거함

# 해당 키 찾기
print('이름' in student) # True
print('주소' in student) # False

singer = {}
singer['이름'] = '트와이스'
singer['구성원수'] = 9
singer['대표곡'] = 'signal'

print(singer)

for i in singer.keys():
    print(f"{i}의 값은 : {singer[i]}")

''' 세트 : 딕셔너리의 특수한 형태 키만 모아놓은것
    중복이 되지 않는다
'''
sett = {1, 1, 2, 3, 4, 5, 5}
print(sett)  # {1, 2, 3, 4, 5}

# 리스트 - > 세트 중복제거
lst = [1, 1, 2, 3, 4, 5, 5, '삼겹살', '고기', '고기']
print(lst)
print(set(lst))


# 두 세트의 교집합 등
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
print(set1 & set2)  #교집합
print(set1 | set2) # 합집합
print(set1 - set2) # 차집합
print(set1 ^ set2) # 대칭 차집합

lst = list(set1 ^ set2)
print(lst)

'''리스트를 정수화'''
# 방법1
lst = [int(i) for i in lst]
lst.sort()
print("정렬된 리스트 : ", lst)

#방법2
lst = list(map(int, lst))
lst.reverse()   #오름차순
print(lst)










