''' 조건문 '''
a = 100
if a < 100:
    print("100보다 작네요")
    print("정말")
elif a == 100:
    print("100과 같다")
else:
    print("100보다 크네요")
print("이건 끝")


''' 반복문 '''
for i in range(0, 3, 1):     # 0부터 3까지 1씩증가하라 for(int i = 0; i <3; i++)와 동일
    print(i,"입니다")
n = 3
while n < 5:
    print('ㅋ', end='') # end=''은 줄바꿈이 안되는 것.
    n += 1

# break 빠져나감
# continue 아래를 가지 않고 올라감
for i in range(1, 10):
    print(i, " 하나 ")
    if(i == 3):
        break
    continue
    print(i, "둘 ")
    break




