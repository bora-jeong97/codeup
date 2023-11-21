
T = int(input())
for i in range(T):  # T만큼 반복
    sum = 0
    lst = list(map(int, input().split()))

    for j in lst:
        if j % 2 == 1:
            sum += j
    print(f"#{i+1} {sum}")
