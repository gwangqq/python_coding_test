str = "JEROEN"


cnt = 0
# tmp = ord(x) - 65
# A = 0 -> +1
# J = 74 -> 74-65 +1
# M = 77 -> 77-65 +1
# Z = 90 -> 91-90

for x in str:
    # print(ord(x))
    tmp = ord(x) - 65
    print(tmp)
    if tmp <= 12:
        cnt += tmp
        print(cnt)
    elif tmp >= 13:
        cnt += (26-tmp)
        print(cnt)

print(cnt + (len(str) - 2))