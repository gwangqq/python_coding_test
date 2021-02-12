n, l = map(int, input().split())
spot = list(map(int, input().split()))

spot.sort()
start = 0
cnt = 0
for s in spot:
    if start < s:
        start = s + l - 1
        cnt += 1
print(cnt)