import sys
sys.stdin = open("./input", "r")


T = int(input())

for test_case in range(1, T+1):
    lst = list(map(int, input().split()))
    sumlst = round(sum(lst)/10)

    print(f"#{test_case} {sumlst}")