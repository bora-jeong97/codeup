data = [1, 1, 0, 0, 0, 1]
# 다중인덱스 반환 방법1
# i, value index와 value
print([i for i, value in enumerate(data) if value == 1])
# 방법 2
l = []
for i, value in enumerate(data):
    if value == 1:
        l.append(i)
print(l)