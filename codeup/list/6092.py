n = int(input())    # 총 횟수
a = list(map(int, input().split()))   # 호출 숫자

lst = [0]*(23+1)
for i in range(n):
    lst[a[i]] += 1

for i in range(1, 24):
    print(lst[i], end=' ')
