import heapq

n = int(input())
nums = []
s = [0]*(1000 + 1)
for i in range(n):
    day, value = list(map(int, input().split()))
    nums.append([-value, day, value])

heapq.heapify(nums)
while nums:
    tmp = heapq.heappop(nums)
    for i in range(tmp[1], 0, -1):
        if s[i] == 0:
            s[i] = tmp[2]
            break
print(sum(s))