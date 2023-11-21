
a = int(input(), 16) # 16진수를 int형으로 변환
print(bin(a))   # 10 -> 2
print(oct(a))   # 10 -> 8
print(hex(a))   # 10 -> 16
print(int(bin(a), 2)) # 2 -> 10
print(int(oct(a), 8)) # 8 -> 10
print(int(hex(a), 16)) # 16 -> 10

print('%o' % a) # 10 -> 8