from collections import deque

# 길찾기니까 BFS


dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
N, M = map(int, input().split()) # N×M크기의 배열로 표현되는 미로

# 1. 0으로 초기화
# 2. 1 세팅
board = [input() for _ in range(N)]

# 길찾기 범위체크 5-3
def is_vaild_coord(y, x):
    return 0 <= y < N and 0 <= x < M


# 5. deque에 값이 없을때까지 돌면서 빼고 넣기 반복
def bfs():
    # 3. 체크 배열 세팅
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True    # 체크배열도 시작 체크하라고 했으니 해준다.

    # 5-1. deque호출
    dq = deque()
    # 5-2. 시작값 세팅
    dq.append((0, 0, 1))    # x, y, 몇칸인지 시작칸부터 시작해서 1
    # 5-3. dq에 값이 없을 떄까지 반복
    while dq:
        #now = dq.popleft()
        # 5-3-1. 빼준 값을 now에 저장
        y, x, d = dq.popleft()

        if y == N-1 and x == M-1:   # 마지막 칸 도달 시 종료
            return d

        nd = d + 1
        # 5-3-2. 전부 돌면서 [now][nxt]에 다음 값이 있는 경우 nxt를 더해준다.
        for k in range(4): # 길찾기라 4방향 k로 nxt를 만들어준다.
            ny = y + dy[k]
            nx = x + dx[k]

            # 길찾기 범위체크 and 1 and 방문체크
            if is_vaild_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, nd))



# 4. 호출
print(bfs())

