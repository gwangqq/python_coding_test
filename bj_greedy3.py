k = int(input())
lope = []
i = 0
while i < k:
    lope.append(int(input()))
    i += 1
lope.sort()

max_w = []
j = 0
while j < k:
    max_w.append(lope[j] * (k-j))
    j += 1
max_w.sort(reverse=True)
print(max_w[0])


