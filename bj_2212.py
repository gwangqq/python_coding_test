n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))

if k >= n:
    print(0)
else:
    dist = []
    for i in range(1, n):
        dist.append(sensor[i] - sensor[i-1])

    dist.sort(reverse=True)
    for _ in range(k - 1):
        dist.pop(0)

    print(sum(dist))

