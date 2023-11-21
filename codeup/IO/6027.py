'''
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.

예시
a = input()
n = int(a)            #입력된 a를 10진수 값으로 변환해 변수 n에 저장
print('%x'% n)  #n에 저장되어있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력

참고
10진수 형태로 입력받고
%x로 출력하면 16진수(hexadecimal) 소문자로 출력된다.
(%o로 출력하면 8진수(octal) 문자열로 출력된다.)

10진법은 한 자리에 10개(0 1 2 3 4 5 6 7 8 9)의 문자를 사용하고,
16진법은 영문 소문자를 사용하는 경우에 한 자리에 16개(0 1 2 3 4 5 6 7 8 9 a b c d e f)의 문자를 사용한다.
16진수 a는 10진수의 10, b는 11, c는 12 ... 와 같다.

>>> bin, ternary operator(42) # 2진수
'0b101010'
>>> oct(42) # 8진수
'0o52'
>>> hex(42) #1 6진수
'0x2a'

>>> int('0b101010', 2)  # 2진수
42
>>> int('0o52', 8)  # 8진수
42
>>> int('0x2a', 16) # 16진수
42

'''

a = int(input())
print('%x' % a) # 16진수 255 -> ff
print('%o' % a) # 8진수