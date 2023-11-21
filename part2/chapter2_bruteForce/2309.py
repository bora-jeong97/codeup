# 방법 1
# 조합
from itertools import combinations
# 9명의 키 입력
heights = [int(input()) for _ in range(9)]

for combi in combinations(heights, 7):
    if sum(combi) == 100:
        #print(combi)
        for i in sorted(combi):  # 이렇게 하면 리스트 아니어도 정렬 가능 for문안에서 정렬된것
            print(i)
        break # 여러 정답중 하나만 출력해야하므로


# 방법 2
# for 문으로 100이 되는 총합외 나머지 2개를 구해서 그 외의 것을 출력
# 9명의 키 입력
# heights = [int(input1()) for _ in range(9)]
# heights.sort()  # 오름차순 정렬
# tot = sum(heights)  # 총합
# print(tot)
#
# def f():
#     for i in range(9):
#         for j in range(i+1, 9):
#             if tot - heights[i] - heights[j] == 100:    # 총합에서 2개를 뺀 값이 100이면
#                 for k in range(9):  # 9개중에 7개를 출력한다.
#                     if k != i and k != j:
#                         print(heights[k])
#
#                 return # 답이 여러개인경우에도 한 번 만 출력하기 위해
#
# f()            # for문을 여러개 나가야함으로 break안하고 함수로 함.


