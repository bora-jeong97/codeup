from collections import deque

# 1.인접행렬 0 초기화
adj = [[0]*(12+1) for _ in range(12+1)]
# 2. 값이 있는 부분에 1 넣어주기
adj[0][1] = adj[0][2] = adj[1][3] = adj[1][4] = 1
adj[3][7] = adj[3][8] = adj[4][9] = adj[2][6] =1
adj[6][10] = adj[6][11] = adj[6][12] =1
adj[2][5] = 1
# i = 0
# for row in adj:
#     print(f"{i} : {row}")
#     i += 1

# 4. 큐에 값이 없을 때까지 빼고 넣어주는 과정 반복
def bfs():
    # 4-1. deque 호출
    dq = deque()
    # 4-2. 시작값 세팅
    dq.append(0) # 시작 노드
    # 4-3. 반복
    while dq:   # dq에 값이 있는 동안 반복
        # 4-3-1. 빼준 값을 now에 저장
        now = dq.popleft() # 빼준값을 now에 저장
        # 4-3-2. 전부 돌면서 [now][nxt]에 다음 값이 있는 경우 nxt를 더해준다.
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)

# 3. 호출
bfs()