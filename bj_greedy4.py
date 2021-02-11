k, n = map(int, input().split())

cnt = 1
while True:
    if n == k:
        break
    elif (n % 2 != 0 and n % 10 != 1) or (n < k):
        cnt = -1
        break
    else:
        if n % 10 == 1:
            n //= 10
            cnt += 1
        else:
            n //= 2
            cnt += 1

print(cnt)

