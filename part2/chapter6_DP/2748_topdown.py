''' 피보나치 수
 top-down 재귀
 '''

# 메모이제이션
cache = [-1] * 91
cache[0] = 0
cache[1] = 1




# top-down 재귀
# 메모이제이션
def f(n):
    if cache[n] == -1:
        cache[n] = f(n - 1) + f(n - 2)

    return cache[n]


print(f(int(input())))