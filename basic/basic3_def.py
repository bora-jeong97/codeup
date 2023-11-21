'''함수 '''
# 함수 선언 부분
def plus(v1, v2):
    result = 0
    result = v1 + v2
    return result

# 전역 변수 부분
hap = 0
# 메인 코드 부분
#if__name__ == '__main__':   # 메인함수 임을 표시 없어도 됨
hap = plus(100, 200)
print("100과 200의 결과는 %d" % hap)

''' global '''
# 함수 선언 부분
def func1():
    global a # a의 전역변수화
    a = 10
    print("func1 : %d " % a)

def func2():
    print("func2 : %d" % a)

a = 20
func1() # 10
func2() # 20 - > 10 global을 씀으로써 변함


''' return 값을 여러개 두는 경우 '''


'''방법 1 return 값을 두개의 변수로 둘다 받아주기 '''
# 함수 선언 부분
def multi(v1, v2):
    res1 = v1 + v2
    res2 = v1 - v2
    return res1, res2

# 전역 변수 부분
hap, sub = 0, 0
myList = []

# 메인 코드 부분
hap, sub = multi(100, 200)
print(hap, sub)




'''방법 2 리스트로 돌리기 '''
# 함수 선언 부분
def multi(v1, v2):
    res1 = v1 + v2
    res2 = v1 - v2
    reList = []
    reList.append(res1)
    reList.append(res2)
    return reList

# 전역 변수 부분
hap, sub = 0, 0
myList = []

# 메인 코드 부분

myList = multi(100, 200)
hap = myList[0]
sub = myList[1]
print(hap, sub)


