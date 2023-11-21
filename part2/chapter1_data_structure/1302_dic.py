# dictionary 사전을 이용해서 k v 로 풀이
d = dict()

# 사전에 k v 입력
for _ in range(int(input())):   # 입력받은 수 만큼 반복
    book = input()
    if book in d:   # key값이 이미 사전에 있다면
        d[book] += 1    # +1
    else:
        d[book] = 1     # 아니면 그냥 1

# print(d.keys())
# print(d.values())
# print(d.items())
# print("d>>> " , d)
# print("가장 큰 값은 ? ", max(d.values()))
#print(isinstance(d. dict)) # 특정 변수가 해당 자료형인지 알수 있는 함수


# 출력 값 담기
result = []
for k, v in d.items():
    if(v == max(d.values())):
        result.append(k)

# print(result)

# 같을 경우 오름차순 사전순
result.sort()
print(result[0])


