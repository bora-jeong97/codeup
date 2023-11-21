'''
BFS Breadth First Search 너비 우선 탐색
큐를 사용해서 구현한다.
완전탐색
리스트로 하면 뒤에서 넣고 앞에서 빼기 때문에
삭제시 O(N)이 되므로 deque를 써준다.
'''
from collections import deque
# 0으로 이차원 행렬 초기화
adj = [[0]*13 for _ in range(13)]
adj[0][1] = adj[0][2] = 1
adj[1][3] = adj[1][4] = 1

def bfs():
    dq = deque()
    dq.append(0)
    while dq:   # 큐에 값이 남아있을 때까지 반복
        now = dq.popleft() # 오른쪽으로 들어오고 왼쪽으로 나간다.
        for nxt in range(13):
            if adj[now][nxt]:  # 값이 존재한다면
                dq.append(nxt)


bfs()