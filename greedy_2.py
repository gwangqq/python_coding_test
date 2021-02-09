# str = "JEROEN"
# str = "JAN"
str = "JAZ"

cnt = 0
# tmp = ord(x) - 65
# A = 0 -> +1
# J = 74 -> 74-65 +1
# M = 77 -> 77-65 +1
# Z = 90 -> 91-90
cnt_a = 0
length = len(str)
for x in str:
    # print(ord(x))
    tmp = ord(x) - 65
    print(tmp)

    if tmp <= 12:
        cnt += tmp
        print(cnt)
        if tmp == 0:
            cnt_a
            print(cnt_a)
    elif tmp >= 13:
        cnt += (26 - tmp)
        print(cnt)

if cnt_a >= 1:
    answer = cnt + (length - 2)
else:
    answer = cnt + length - 1

print(answer)
