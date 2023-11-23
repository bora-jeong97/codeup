s = ord("a")
e = ord(input())
#print(f"시작 {s} 끝 {e}")

while s <= e:
    print(chr(s))
    s+=1

'''
ord( ) 는 어떤 문자의 순서 위치(ordinal position) 
print(chr(c))  #c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다.

영문 소문자(a ~ z) 1개가 입력되었을 때,
a부터 그 문자까지의 알파벳을 순서대로 출력해보자.

예시
c = ord(input())
t = ord('a')
while t<=c :
  print(chr(t), end=' ')
  t += 1

참고
알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있다.
chr(정수값)을 이용하면 유니코드 문자로 출력할 수 있다.
print(..., end=' ') 와 같이 작성하면 값 출력 후 공백문자 ' '를 출력한다. 즉, 마지막에 줄을 바꾸지 않고 빈칸만 띄운다.
(end='\n'로 작성하거나 생략하면, 값을 출력한 후 마지막(end)에 줄바꿈(newline)이 된다.)
'''