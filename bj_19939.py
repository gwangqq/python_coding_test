n, k = map(int, input().split())

i = 1
sum = 0
while i <= k:
    sum += i
    i += 1

if n - sum < 0:
    print(-1)
else:
    if (n - sum) % k == 0:
        print(k-1)
    else:
        print(k)