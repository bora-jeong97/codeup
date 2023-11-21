'''
DFS Depth First Search 깊이 우선 탐색
스택 or 재귀
완전탐색이기 때문에 모든 노드를 탐색한다.
리스트로 해도 뒤에서 넣고 뒤에서 빼기 때문에
삽입 삭제가 O(1)
'''
adj = [[0]*13 for _ in range(13)]    # adjacent 인접한
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
for row in adj:
    print(row)


def dfs(now):
    for next in range(13):
        if adj[now][next]:  # 값이 존재하면 값이 0이 아니면
            dfs(next)


dfs(0) # 시작노드 값을 넣어준다.