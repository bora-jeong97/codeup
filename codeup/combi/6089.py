a, r, n = map(int, input().split())


s = a   # 시작값
for i in range(0, n-1):   # n번 반복 시작값도 포함해야해서 -1해준다.
    s *= r  # r을 곱해준다.
    # print(s)

print(s)