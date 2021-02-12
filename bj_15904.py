words = input()
check = ['U', 'C', 'P', 'C']
flag = True

for i in check:
    n = words.find(i)
    if n:
        words = words[n:]
        flag = True
    else:
        flag = False

if flag:
    print('I love UCPC')
else:
    print('I hate UCPC')