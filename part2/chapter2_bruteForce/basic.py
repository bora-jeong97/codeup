# 완전탐색
# 브루트 폴스 brute force
'''
완전탐색의 대표적 알고리즘은 아래와 같다.
브루트 폴스 brute force : 무차별 대입 모든 경우의 수를 구한다.
    N개의 수를 입력 받아서 두 수를 뽑아 합이 가장 클 때는?
    시간제한 : 1초, 입력 2 <= n <= 1,000,000
    NC2 이기 때문에 시간복잡도는 O(N**2) 시간복잡도가 높기 때문에 N개의 수가 클 경우에
    사용할 수 없다.
    -> 그렇다면 완전탐색은 안될거같다.  모든 경우의 수를 할 수 없고
    그렇다면 정렬(O(NlongN)을 사용할 수 있을 것 같다.
    정렬을 해서 가장 큰 수와 그 전까지 큰 수를 가지고 풀면 된다.
'''
# 순열
'''
모든 경우의 수를 순서대로 살펴볼 때 용이하다
삼성에서 next_permutation 활용하면 쉽게 풀리는 문제들이 많이 나왔다고 한다.
0! == 1
'''
from itertools import permutations
v = [0, 1, 2, 3]

lst = []
for i in permutations(v, 4):    # permutations(리스트, 몇가지)몇가지를 뽑는지
    lst.append(i)
    print(i)
print(len(lst)) # 4 * 3 * 2 * 1

#  조합
'''
순서상관 없는 경우의 수 
'''
from itertools import combinations

v = [0, 1, 2, 3]
print("조합------------------------")
lst = []
for i in combinations(v, 4):
    lst.append(i)
    print(i)
print(len(lst))



