import heapq

n, k = map(int, input().split())
line = list(map(int, input().split()))

difference = []

for i in range(1, len(line)):
    difference.append(line[i]-line[i-1])

heapq.heapify(difference)
result = 0

for i in range(n-k):
    result += heapq.heappop(difference)
print(result)
