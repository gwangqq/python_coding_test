n = int(input())
s = list(map(int, input().split()))
c = list(map(int, input().split()))


total = s[0] * c[0]
start = c[0]
distance = 0

for i in range(1, n-1):
    if c[i] < start:
        total += c[i] * distance
        start = c[i]
        distance = s[i]
    else:
        distance += s[i]

    if i == n - 2:
        total += start * distance
print(total)