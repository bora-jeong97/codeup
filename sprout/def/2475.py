
a, b, c, d, e = map(int, input().split())
print((a**2 + b**2 + c**2 + d**2 + e**2) % 10)

'''다른사람 풀이
print(sum(int(i)**2 for i in input1().split())%10)
'''