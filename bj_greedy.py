array = [500, 100, 50, 10, 5, 1]
K = 1000 -  int(input())
cnt = 0
for i in array:
    cnt += K // i
    K %= i
print(cnt)