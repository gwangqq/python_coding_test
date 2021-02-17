l, p, v = map(int, input().split())
if l != 0 and p != 0 and v != 0:

    result = 0
    tmp = v//p
    tmp2 = v % p

    result = (l * tmp)
    if tmp2 >= l :
        print(result + l)
    else:
        print(result + tmp2)

