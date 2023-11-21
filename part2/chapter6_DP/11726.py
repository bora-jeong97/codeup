''' 2 x n 타일링
점화식을 만든다. 점화식 : f(n) = f(n-1) + f(n-2)
'''

MOD = 10_007    # _는 콤마대신 쓰는 방법 안써도 됨

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

n = int(input())
for i in range(3, 1001):
    dp[i] = (dp[i-1] + dp[i-2]) % MOD


print(dp[n])

