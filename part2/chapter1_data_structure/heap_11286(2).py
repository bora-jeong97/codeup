import sys
import heapq as hq
# 우선순위큐
# 방법 2. x값 그대로
# chapter1 자료구조  - 예제문제(3)ㄹㅇㄱㄹㅀ
input = sys.stdin.readline

# 입력
plus_heap = [] # 양수
minus_heap = [] # 음수

for _ in range(int(input())):   # 해당 값의 횟수만큼 반복
    x = int(input())

    if x :  # 0이 아니라 값이 있을 때
        if(x > 0):
            hq.heappush(plus_heap, -x)
        else:
            # 양수화 해서 넣는다. 절대값 비교를 위해 음수는 원래 큰 수가 작은거니까 양수화 해서 넣어준다. 음수의 가장 큰 값이 왼쪽으로 간다.
            hq.heappush(minus_heap, -x)

print("min_heap : ", plus_heap)
print("max_heap : ", minus_heap)

print("plus_heap[0] : ", -plus_heap[0])
print("plus_heap[1] : ", -plus_heap[1])
print("plus_heap[2] : ", -plus_heap[2])

'''
min_heap :  [1, 2]
max_heap :  [-3, -1, -2]
'''
