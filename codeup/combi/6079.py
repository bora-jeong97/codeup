

n = int(input())

sum = 0
for i in range(n):
    if sum < n:
        sum += i
    if sum >= n:
        print(i)
        break

