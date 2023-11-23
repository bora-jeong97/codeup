R, G, B = map(int, input().split())

sum = 0
for r in range(R):
    for g in range(G):
        for b in range(B):
            print(r, g, b)
            sum += 1

print(sum)