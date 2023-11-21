import sys
sys.stdin = open("./input", "r")

# 총 10번 반복
for test_case in range(10):

    re = 0
    board = [[0] * 1000 for _ in range(255)]

    N = int(input()) # 건물개수
    lst = list(map(int, input().split()))

    # 1세팅
    for x in range(N): # 개수
        if lst[x] != 0:
           for y in range(lst[x]): #높이
               board[y][x] = 1


    ans = 0

    # 보드판 내에 1이 있으면 조망권 검사
    for yy in range(255):
        for xx in range(1000):
            if board[yy][xx]:
                if board[yy][xx-1] == 0 and board[yy][xx-2] == 0 and board[yy][xx+1] == 0 and board[yy][xx+2] == 0:
                    ans += 1


    # 출력
    print(f"#{test_case+1} {ans}")