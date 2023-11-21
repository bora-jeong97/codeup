import sys
# 빠른 입출력
input = sys.stdin.readline
sys.stdin = open("./input", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = []
    max = 0

    # 보드 생성
    for _ in range(n):
        tmp_list = [*map(int, input().split())]
        board.append(tmp_list)

    # for row in board:
    #     print(row)

    # 시작점
    for i in range(0, n - m + 1):   # 마지막 좌표를 구하기 위해 ex) 5, 2면 3,3이 마지막 처음 시작 좌표
        for j in range(0, n - m + 1):
            tmp = 0

            # 시작점부터 파리채 범위까지의 합
            for k in range(i, i + m):
                for l in range(j, j + m):
                    tmp += board[k][l]

            if tmp > max:
                max = tmp

    print(f"#{test_case} {max}")