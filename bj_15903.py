import heapq

n, m = map(int, input().split())
tmp = list(map(int, input().split()))
num = []
for i in range(n):
    heapq.heappush(num, tmp[i])

j = 0

while j < m:
    tmp_1 = heapq.heappop(num)
    tmp_2 = heapq.heappop(num)
    heapq.heappush(num, tmp_1 + tmp_2)
    heapq.heappush(num, tmp_1 + tmp_2)
    j += 1

total = 0
for _ in num:
    total += _

print(total)