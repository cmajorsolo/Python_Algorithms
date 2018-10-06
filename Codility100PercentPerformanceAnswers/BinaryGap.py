def solution(N):
    binaryN = '{0:b}'.format(N)
    if '0' not in binaryN:
        return 0
    index = [i for i, e in enumerate(binaryN) if e == '1']
    gap = [y - x for x, y in zip(index, index[1:])]
    if len(gap) is 0:
        return 0
    else:
        return max(gap) - 1

if __name__== '__main__':
    print(solution(1041))
    print(solution(9))