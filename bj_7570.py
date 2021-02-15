n = int(input())
nums = list(map(int, input().split()))
nums.insert(0,0)

positions = [0] * (n+1)
for i in range(1, len(nums)):
    positions[nums[i]] = i
print(nums)
print(positions)
count = 1
max = -1
for i in range(1, len(nums) - 1):

    if positions[i] < positions[i+1]:
        # print("positions[%d]: %d" % (positions[i], positions[i]))
        count += 1
        if count > max:
            max = count
    else:
        count = 1
    print("count : %d" % count)
    print(max)
print(n - max)
