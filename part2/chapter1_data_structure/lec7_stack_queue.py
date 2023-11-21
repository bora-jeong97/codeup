'''스택 stack
삽입/삭제: O(1)
FILO first in last out
LIFO 후입선출
'''
# 파이썬은 스택구현을 그냥 리스트로 사용하면 된다.
s = []
s.append(123)   # insert
s.append(456)
s.append(789)
print("스택 Stack")
print("size : ", len(s))

while len(s) > 0:
    print(s[-1])    # 가장 마지막 index가 -1부터 센다.
    s.pop(-1)   # delete pop()도 맨 끝(오른쪽)에 있는 것 삭제


''' 큐 Queue
삽입/삭제: O(1)
FIFO/LILO 선입선출
'''
# 큐가 느리기 때문에 deque덱을 사용하면 빠르다
from collections import  deque

dq = deque()    # 덱은 양쪽에서 넣을 수 있다.
dq.append(123) # 123
dq.append(456) # 456 123
dq.append(789) # 789 456 123
print("큐 Queue ")
print("size : ", len(dq))

while len(dq) > 0:
    print("남은 큐 : ", dq)
    print(dq.popleft())


'''우선순위 큐
  from queue import PriorityQueue # 느림
'''
print("우선순위 Priority Queue(Heap) ")


import heapq as hq
pq = []
hq.heappush(pq, 456)
hq.heappush(pq, 123)
hq.heappush(pq, 789)
print("size: ", len(pq))
print("pq :  ", pq)
while len(pq) > 0:
    print("최상단 노드 : ", pq[0])
    print(hq.heappop(pq))   # 최상단 노드부터 삭제됨.


