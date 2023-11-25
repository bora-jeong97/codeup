
'''
설탕과자
https://www.codeup.kr/problem.php?id=6097
막대를 놓는 방향(d:가로는 0, 세로는 1)
첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
1 <= w, h <= 100
1 <= n <= 10
d = 0 or 1
1 <= x <= 100-h
1 <= y <= 100-w

'''
h, w = map(int, input().split())
board = [[0 for _ in range(w)] for _ in range(h)]



for _ in range(int(input())):
    l, d, x, y = map(int, input().split())

    if d == 0:  # 가로
        for _ in range(l):  # 길이 만큼 반복
            board[x-1][y-1] = 1
            y += 1
    elif d == 1:   # 세로
        for _ in range(l):
            board[x-1][y-1] = 1
            x += 1
# print(f"w : {w} h : {h} board 길이 : {len(board)} {len(board[0])}")

for i in range(h):
    for j in range(w):
        print(board[i][j], end=' ')
    print()

