import sys
sys.stdin = open("./input", "r")
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
# 1.인접행렬 0 초기화
adj = [[0]*N for _ in range(N)]

# 2.값이 있는부분에 1넣어줄기
for _ in range(M):
    a, b = map(lambda x : x-1, map(int, input().split()))   # 간선이 1부터 들어오니까 인덱스와 맞춰주기 위해
    adj[a][b] = adj[b][a] = 1   # 양방향

for row in adj:
    print(row)

# 3. 체크 배열
ans = 0 # 연결요소
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:  # 값이 있고 체크가 아니라면
            chk[nxt] = True
            dfs(nxt)

# 호출 시작 노드(now)
for i in range(N):
    if not chk[i]:  # 체크가 안된 노드라면 False 처음 하는 거라면
        ans += 1    # 연결요소 +1
        chk[i] = True   # 체크
        dfs(i)

print(ans)

# for row in adj:
#     print(row)