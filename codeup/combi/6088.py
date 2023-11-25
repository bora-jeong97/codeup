s, d, n = map(int, input().split())

cnt = 1
num = s
while cnt < n:
    cnt += 1
    num += d


print(num)


'''
a,d,n = map(int,input().split())
total=a
for i in range(0,n-1):
    total=total+d
print(total)
'''