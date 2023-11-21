'''맵 Map(DIctionary)
key Value
삽입/삭제
    c++ : O(log N) / rea-black tree
    python : O(1) / hash
'''
print("맵 Map(DIctionary)")
m = {}
m["yoondy"] = 40
m["sky"] = 100
print("size: ", len(m))
for k in m:
        print(k, m[k])


'''집합 Set
중복을 허용하지 않는다.
삽입/삭제
    c++ : O(log N)
    python : O(1) 
'''
print("집합 Set")
s = set()
s.add(123)
s.add(234)
s.add(123)
s.add(567)

print("size : ", len(s))
print("s : ", s)
s.remove(123)
print("s : ", s)

for i in s:
    print("i : ", i)


