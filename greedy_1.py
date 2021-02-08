n = 5
lost = [1, 3, 5]
reserve = [2, 4]


def solution(n, lost, reserve):
    _lost = list(set(lost) - set(reserve))
    _reserve = list(set(reserve) - set(lost))

    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


print(solution(n, lost, reserve))
