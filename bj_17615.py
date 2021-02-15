n = int(input())
balls = input()


ball_array = []
for i in balls[::-1]:
    ball_array.append(i)

tmp = ball_array[0]
start = 0
for i in range(1, n):
    if ball_array[i] != tmp:
        start = i
        break
r = 0
b = 0
for i in ball_array[start:]:
    if i == 'R':
        r += 1
    else:
        b += 1
if r <= b:
    print(r)
else:
    print(b)

ball_array2 = []
for i in balls[1::]:
    ball_array2.append(i)

tmp2 = ball_array2[0]
start2 = 0
for i in range(1, n):
    if ball_array2[i] != tmp2:
        start2 = i
        break
r2 = 0
b2 = 0
for i in ball_array2[start2:]:
    if i == 'R':
        r2 += 1
    else:
        b2 += 1
if r2 <= b2:
    print(r2)
else:
    print(b2)




