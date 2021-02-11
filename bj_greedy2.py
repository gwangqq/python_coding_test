a = input().split('-')
result = 0
num = []
for i in a:
    s = i.split('+')
    tmp = 0
    for j in s:
        tmp += int(j)
    num.append(tmp)
n = num[0]
for x in range(1, len(num)):
    n -= num[x]

print(n)
