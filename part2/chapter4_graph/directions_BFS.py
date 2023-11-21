'''길찾기 문제(최단거리 == bfs)
방향값을 미리 코드에 짜두고 for문으로 순회하는 기법을 꼭 익혀두자
방문체크 필요
각 칸이 노드
상하좌우 4방향의 간선
'''
from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
chk = [[False] * 100 for _ in range(100)]   # 방문체크
N = int(input())

# 갈 수 있는 범위인지 유효한 칸인지 체크
def is_valid_coord(y, x):   # vaildation체크 y,x가 0보다 크면서 주어진 값을 벗어나지 않는지 체크
    return 0 <= y < N and 0 <= x < N

def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))    # 시작 값
    while len(q) > 0:   # 큐에 값이 존재하는 동안 반복
        y, x = q.popleft()  # 가장 왼쪽값을 빼준다.
        chk[y][x] = True # 방문체크 해당 값 방문했음
        for k in range(4):  # 위 아래 왼쪽 오른쪽 총 4개
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx]:  # 방문한적이 없고 정상루트라면
                q.append((ny, nx))
        