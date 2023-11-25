a, m, d, n = map(int, input().split())



for _ in range(n-1): # n번 반복
    a = a * m + d

print(a)