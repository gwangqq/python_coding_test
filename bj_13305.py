import heapq

n = int(input())
d = list(map(int, input().split()))
tmp = list(map(int, input().split()))

i = 1
first = d[0] + tmp[0]
m = []
start = 0
total = first
while i < n-1:
    if tmp[start] >= tmp[start + 1]:
        start += 1
    total += tmp[start] * d[i]
    print(total)
    i += 1
print(total)



# while i < n - 1:
#
#     if c[i] <= c[i+1]:
#         total += c[i] * d[i]
#         total += c[i] * d[i+1]
#     else:
#
#     i += 1