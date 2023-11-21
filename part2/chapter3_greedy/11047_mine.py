import sys
##  주의
## 아래는 시간초과가 나는 코드임
## 왜냐 동전값이 10의 6승인 백만원 하나랑 1원 하나일경우 N제곱이 되면서
# 10의 12승이 되니까 시간초과가 난다. 이럴 때 나누기와 몫으로 해야한다.
N, K = map(int, input().split())
lst = [int(sys.stdin.readline()) for _ in range(N)]
lst.reverse()

cnt = 0 # 필요한 동전 수

for i in lst:
    if K == 0:
        break
    if (i != 0 and i <= K):  # i가 0이 아니고 남은돈보다 작거나 같을 때
        while i <= K:
            K -= i
            cnt += 1
        # print(f'동전 : {i} 남은 돈: {K} 총 수: {cnt}')
print(cnt)





