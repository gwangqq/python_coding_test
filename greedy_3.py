number = "1924"
k = 2

# k 자리 수 만큼 첫 숫자 비교
# k자리 수 -> 뒤에나온 숫자가 크면 앞에 자리 삭제, 같거나 작으면 유지 -> k - 1
fore = sorted(list(number[:k + 1]), reverse=True)

print(fore)


i = 1
# while i <= len(number):
#     print(number.index(i))
#     i += 1
