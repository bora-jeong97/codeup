# -*- coding: utf-8 -*-

import sys
''' 입출력 '''
# n = input1() # 한줄을 모두 입력 공백포함, input은 무조건 문자열을 반환함
# print(n)

''' 인트화 '''
# n = int(input1())
# print(n+4)

''' 한줄에 여러개 '''
# 묶임, string
# n = input1().split()
# print(n)
# 각자
# a, b = map(int, input1().split()) # 형변환 int, 쪼개기
# print(a)
# print(b)


'''빠른 입출력 함수'''
#15552.빠른 A+B 백준 참고
for _ in range(3):
    n = int(sys.stdin.readline()) # 한줄씩 입력
    print(n)




# 1.
# import sys
# n = int(sys.stdin.readline())
# print("값은? ", n)

# 2.
# from sys import stdin
#
# n = int(stdin.readline())
# print(n)

#3
# from sys import stdin
# input1 = stdin.readline
#
# n = int(input1())
# print(n)

# 내 픽
import sys
input = sys.stdin.readline

#a, b = input1().split()             # 문자열
a, b = map(int, input().split())    # 수
print(a)
print(b)
