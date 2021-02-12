g = int(input())
p = int(input())
i = 0
plane = []
d = {}
cnt = 0
docking = 0
while i < p:
    plane.append(int(input()))
    i += 1

print(len(set(plane)))

# for x in plane:
#     if x not in d:
#         d[x] = 1
#         cnt += 1
#     elif x in d:
#         d[x] = 1

