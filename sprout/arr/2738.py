import sys

y, x = map(int, sys.stdin.readline().split())

lst1 = []
lst2 = []
tmp = []

# 첫 행렬 입력
for i in range(0, y):
    tmp =list(map(int, sys.stdin.readline().split()))
    lst1.append(tmp)
    tmp = []

#print(lst1)
# 두번째 행렬 입력
for i in range(0, y):
    tmp =list(map(int, sys.stdin.readline().split()))
    lst2.append(tmp)
    tmp = []
#print(lst2)

# 출력
for i in range(0, y):
    for j in range(0, x):

        print(f"{lst1[i][j] + lst2[i][j]}", end=" ")
    print("")
#arr = [[int(i) for i in range(0, x)] for j in range(0, y)]
#print(arr)


'''
1등 코딩 
import sys
I = sys.stdin.readline

N,M=map(int,I().split())
A=[]
B=[]
for _ in range(N):
    A.append(list(map(int,I().split())))
for _ in range(N):
    B.append(list(map(int,I().split())))
    
for i in range(N):
    a=[A[i][j]+B[i][j] for j in range(M)]
    print(*a)

'''

