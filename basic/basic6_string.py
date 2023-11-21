'''문자열(불변성 데이터 형식)'''
ss = "자료구조&알고리즘"
print(ss[0])
print(ss[1:4])
print(ss[4:])

print('파이썬'+'최고')
print('파이썬'*3)
print(len('파이썬'))

ss = '파이썬 공부는 즐겁습니다, 물론 모든 공부가 다 재미있지는 않죠. ^^'
print(ss.count('공부'))

print(ss.index('공부')) # 왼쪽에서부터 처음으로 맞닫뜨리는 인덱스를 찾는다.
print(ss.rindex('공부')) # 오른쪽에서부터 처음으로 맞닫뜨리는 인덱스를 찾는다.
print(ss.index('공부', 5)) #5번 인덱스 부터 찾는다.
print(ss.find('없는것'))   #없는 문자를 찾으라고 하면 -1을 반환

print(ss.find('공부')) #
print(ss.find('공부', 5)) # 5번 인덱스 부터 찾는다.
print(ss.find('없는것'))   #없는 문자를 찾으라고 하면 -1을 반환

print(ss.startswith('파이썬')) # 해당 문자로 시작하는지
print(ss.startswith('파이썬', 10)) # 10번째 인덱스가 해당 문자로 시작하는지
print(ss.startswith('공부', 21))
print(ss.endswith('^^'))    # 해당 문자로 끝나는지


# 문자열 분리와 결합
ss = 'python을 열심히 공부 중'
print(ss.split()) # 공백단위로 쪼개서 리스트화
ss = '하나,둘,셋'
print(ss.split(','))    # 지정할 수 있음

ss = '원\n투\n쓰리'
print(ss)
print(ss.splitlines())# 라인별로 쪼갠다

ss = '%'
print(ss.join('파이썬')) # 문자열 사이사이에 넣는다

'''함수이름 대입'''
# map(합수이름, 리스트 이름)
before = ['2022', '12', '31'] # 문자열
after = list(map(int, before)) # 정수
print(after)

'''튜플
읽기 전용 값 변경 불가'''
#방법1
tt1 = (10, 20, 30); print(tt1)  # 파이썬에서 ;는 행이 넘어가는 효과가 있음
#방법2
tt2 = 10, 20, 30
print(tt2)

tt3 = (10,)   # 튜플을 하나짜리를 만들고 싶으면 뒤에 ,를 해준다
print(tt3)

# 튜플은 읽기 전용이므로 아래는 모두 안된다
#tt1.append(0)
#tt1[0] = 40

# 통째로 삭제는 가능
print("살아있음 ", tt1)
del(tt1)
#print(tt1)

# 읽기는 리스트와 동일하게 가능
tt1 = (1, 5, 10, 15)
print(tt1[2])
print(tt1[0:2])

tt2 = ('a', 'b')
print(tt1+tt2) # 튜플끼리 더하는것 가능
print(tt2*3) # 곱하기도 가능

# 튜플은 변환할 수 없기 때문에 리스트화 하고 가져오면 된다.
myTuple = (10, 20, 30)
myLst = list(myTuple)
myLst.append(40)
myTuple = tuple(myLst)
print(myTuple)

