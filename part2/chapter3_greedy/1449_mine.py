import sys
sys.stdin = open("./input", "r")

# L - lst가 0 이 아닌경우 붙일 수 있음

N, L = map(int, input().split())

#widths = [int(input) for _ in range(N)]
n = map(int, input().split())
for i in n:
    print(i)
#
# for i in widths:
#     n = L # 나머지 값
#
#     print(f'n의 값은 {n}')