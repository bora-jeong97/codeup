import sys
sys.stdin = open("./input", "r")

N, L = map(int, input().split()) # 물이 세는 곳의 개수, 테이프의 길이

# 전체좌표 표기 fasle로 초기화
coord = [False] * 1001 # [False, False, False, False, False, False, False, False, False, False, False]

# 해당좌표
for i in map(int, input().split()):
    coord[i] = True # 해당좌표만 True라고 함

ans = 0 # 남은 좌표
x = 0 # 현재 좌표
while x < 1001:

    if coord[x]:
        ans += 1
        x += L
    else:
        x += 1

print(ans)
