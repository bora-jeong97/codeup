'''
DFS : 깊이 우선 탐색
스택 / 재귀를 사용해서 구현한다.
'''

#adjacent 인접한
# 1.인접행렬 0 초기화
adj = [[0]*13 for _ in range(13)]
# 2. 값이 있는 부분에 1 넣어주기
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
adj[2][3] = adj[2][4] = 1
adj[5][6] = 1
adj[7][8] = adj[7][9] = 1
adj[9][10] = adj[9][11] = adj[9][12] = 1


# for row in adj:
#     print(row)

# 4. 재귀 [now][nxt] 값이 있을때까지 반복 호출
def dfs(now):
    for nxt in range(13): # nxt는 다음 방문할 노드
        if adj[now][nxt]: # 값이 잇으면
            dfs(nxt)
# 3. 시작노드 설정
dfs(0)  # 시작 노드