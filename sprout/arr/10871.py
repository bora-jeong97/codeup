
'''
10 5
1 10 4 9 2 3 8 5 7 6
'''
n, x = map(int, input().split())
arr = map(int, input().split())
arr = list(arr)
for i in range(0, n):
    if(arr[i] < x):
        print(arr[i], end=' ')