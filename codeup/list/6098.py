board = []
# 1. board 세팅
for _ in range(10):
    board.append(list(map(int, input().split())))

y = 1
x = 1

# 2. 입력

for _ in range(100):
    if y == 8 and x == 8:
        if board[y][x] == 0 or board[y][x] == 2:
            board[y][x] = 9
            break
        else: # 1이면
            break

    if board[y][x] == 0:
        board[y][x] = 9
        x += 1
    elif board[y][x] == 1:
        x -= 1
        y += 1
    elif board[y][x] == 2:   # 2라면 끝냄
        board[y][x] = 9
        break




# 3. 출력
for i in range(10):
    for j in range(10):
        print(board[i][j], end=' ')
    print()