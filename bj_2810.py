N = int(input())
seats = input()

holder = 0
holder += seats.count('S')
holder += seats.count('LL')
if holder >= N:
    print(N)
else:
    print(holder + 1)