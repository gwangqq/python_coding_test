N, K = map(int, input().split())
value_list = [int(input()) for _ in range(N)]

value_list.sort(reverse=True)

cnt = 0
for i in value_list:
    cnt += K // i
    K %= i
print(cnt)