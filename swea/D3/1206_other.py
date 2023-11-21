import sys
sys.stdin = open("./input", "r")

for test_cast in range(1, 11):
    result = 0
    houseCount = int(input())   #집 수
    house = list(map(int, input().split())) # 집들의 높이

    for i in range(2, houseCount-2):
        def_2 = house[i] - house[i-2]
        def_1 = house[i] - house[i-1]
        def1 = house[i] - house[i+1]
        def2 = house[i] - house[i+2]
        if def_2 > 0 and def_1 > 0 and def1 > 0 and def2 > 0 :
            result += min(def_2, def_1, def1, def2)

    print("#{} {}".format(test_cast, result))