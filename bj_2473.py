import heapq
import sys

n = int(input())
weight = list(map(int, input().split()))
weight.sort()
num = 1

for i in range(n):
    if num < weight[i]:
        print("break num: %d weight : %d" % (num, weight[i]))
        break
    print(weight[i])
    num += weight[i]

print(num)