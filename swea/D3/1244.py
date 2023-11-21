'''교환은 무조건 해야함
크기가 크지 않아도 무조건 해야함
9 4 > 4 9
'''
import sys
sys.stdin = open("./input", "r")

T = int(input())

for test_case in range(1, T+1):
    result = ""
    board, cnt = input().split()
    cnt = int(cnt)
    board = list(board)

    for i in range(cnt):
        maxNum = max(board)
        minNum = min(board)
        maxIndex = board.index(maxNum)
        minIndex = board.index(minNum)

        tmp = board[maxIndex]
        board[maxIndex] = board[minIndex]
        board[minIndex] = tmp

        print(f"{i+1} 시도 : max {maxNum} min {minNum}")
        result = ''.join(board)
        print(result)
    print(f"#{test_case} {result}")