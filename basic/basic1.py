
''' 타입 '''
a = 5
b = "5"
c = 5.0

print("a의 타입 : ", type(a))
print("b의 타입 : ", type(b))
print("c의 타입 : ", type(c))

# 슬라이싱 구간 만큼의 범위를 가져온다.
aa = ['a', 'b', 'c']
print(aa[0:2]) # 0부터 2-1의 인덱싱까지 총 2개 가져옴 ['a', 'b']

''' 반복문 (for, while)
    for i in 리스트 : 리스트 안에 있는 값 i에 대해서 
'''

num = 0

while num < 5:
    print(num)
    num = num+1

'''남친몬'''
a = 3
# 제일 나은 방식
print(f"{a} + 1 = {a + 1}") # f스트링
# 그 다음 괜찮은 방식
print("{} + 1 = {}".format(a, a + 1))
# 좀 힘든 방식
print("%d + 1 = %d" % (a, a + 1))




boolVar, intVar, floatVar, strVar = True, 0, 0.0, ""

print(type(boolVar))
print("%d" % (100+100))
print("%d %d %f %c %s" % (100, 200, 2.0, 'a', "가나다")) # %c : 캐릭터, %s :  문자열

# 입출력
#var1 = input1('숫자-->') # input1()은 문자열 설명도 쓸수 있음 숫자화 하려면 int(input1())

a = 5/3  # 진짜 나누기임 실수화
print(a)

#a = 5//3 # 정수화 하는 나누기 수소점 버림
#print(a)

b = 2
print("제곱 : ", b**3)

import math
print(math.ceil(a)) # 올림
print(math.floor(a)) # 내림 바닥
print(round(a))  # 반올림

a = 100
a = a+1
a += 1 # 위아래가 동일함
# 파이썬은 ''와 ""이 동일함
# 파이썬은 long없음 int만 쓰면됨
s1, s2, s3 = "100", "100.123", "999999999999"
print(s1, s2, s3)
print(int(s1), float(s2), int(s3))










