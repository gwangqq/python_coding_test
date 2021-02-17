import heapq

n = int(input())
cost = []
for i in range(n):
    tmp = int(input())
    cost.append([-tmp, tmp])
# print(cost)
heapq.heapify(cost)

result = 0
j = 0
while j < n:
    if (j + 1) % 3 == 0:
        heapq.heappop(cost)
    else:
        tmp1 = heapq.heappop(cost)
        result += tmp1[1]
    j += 1

print(result)